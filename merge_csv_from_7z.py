#!/usr/bin/env python3
import argparse
import csv
import re
import subprocess
import tempfile
from collections import OrderedDict
from pathlib import Path
from typing import Dict, List, Tuple


def normalize_header(name: str) -> str:
    name = (name or "").strip().lower()
    name = re.sub(r"[^a-z0-9]+", "_", name)
    name = re.sub(r"_+", "_", name).strip("_")
    return name or "unnamed_column"


def detect_encoding_and_delimiter(file_path: Path) -> Tuple[str, str]:
    sample_bytes = file_path.read_bytes()[:8192]
    encoding = "utf-8-sig"
    try:
        sample_text = sample_bytes.decode(encoding)
    except UnicodeDecodeError:
        encoding = "latin-1"
        sample_text = sample_bytes.decode(encoding, errors="replace")

    delimiter = ","
    try:
        dialect = csv.Sniffer().sniff(sample_text, delimiters=",;\t|")
        delimiter = dialect.delimiter
    except csv.Error:
        if ";" in sample_text and sample_text.count(";") >= sample_text.count(","):
            delimiter = ";"

    return encoding, delimiter


def extract_archive(archive_path: Path, password: str, target_dir: Path) -> None:
    cmd = [
        "7z",
        "x",
        "-y",
        f"-p{password}",
        str(archive_path),
        f"-o{target_dir}",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        raise RuntimeError(
            "Kon archive niet uitpakken met 7z. Controleer wachtwoord en bestand.\n"
            f"7z stderr:\n{result.stderr}\n7z stdout:\n{result.stdout}"
        )


def build_source_metadata(csv_files: List[Path]) -> Tuple[List[str], Dict[str, Dict[str, str]], List[dict]]:
    unified_columns: List[str] = []
    source_to_column_map: Dict[str, Dict[str, str]] = {}
    source_stats: List[dict] = []

    for file_path in csv_files:
        source_file = file_path.name
        encoding, delimiter = detect_encoding_and_delimiter(file_path)

        with file_path.open("r", encoding=encoding, newline="") as infile:
            reader = csv.DictReader(infile, delimiter=delimiter)
            if not reader.fieldnames:
                source_to_column_map[source_file] = {}
                source_stats.append(
                    {
                        "source_file": source_file,
                        "encoding": encoding,
                        "delimiter": delimiter,
                        "rows": 0,
                    }
                )
                continue

            original_headers = list(reader.fieldnames)
            normalized_map: Dict[str, str] = OrderedDict()
            used_names = set()

            for header in original_headers:
                base = normalize_header(header)
                candidate = base
                suffix = 2
                while candidate in used_names:
                    candidate = f"{base}_{suffix}"
                    suffix += 1
                used_names.add(candidate)
                normalized_map[header] = candidate

            for normalized in normalized_map.values():
                if normalized not in unified_columns:
                    unified_columns.append(normalized)

            row_count = sum(1 for _ in reader)

        source_to_column_map[source_file] = dict(normalized_map)
        source_stats.append(
            {
                "source_file": source_file,
                "encoding": encoding,
                "delimiter": delimiter,
                "rows": row_count,
            }
        )

    return unified_columns, source_to_column_map, source_stats


def merge_csv_files(
    csv_files: List[Path],
    output_path: Path,
    output_delimiter: str,
    unified_columns: List[str],
    source_to_column_map: Dict[str, Dict[str, str]],
) -> int:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = ["source_file"] + unified_columns
    merged_rows = 0

    with output_path.open("w", encoding="utf-8", newline="") as outfile:
        writer = csv.DictWriter(
            outfile,
            fieldnames=fieldnames,
            delimiter=output_delimiter,
            quoting=csv.QUOTE_MINIMAL,
        )
        writer.writeheader()

        for file_path in csv_files:
            source_file = file_path.name
            source_map = source_to_column_map[source_file]
            encoding, delimiter = detect_encoding_and_delimiter(file_path)

            with file_path.open("r", encoding=encoding, newline="") as infile:
                reader = csv.DictReader(infile, delimiter=delimiter)
                if not reader.fieldnames:
                    continue

                for row in reader:
                    merged = {"source_file": source_file}
                    for key in unified_columns:
                        merged[key] = ""
                    for original_col, value in row.items():
                        normalized_col = source_map.get(original_col)
                        if normalized_col:
                            merged[normalized_col] = value if value is not None else ""
                    writer.writerow(merged)
                    merged_rows += 1

    return merged_rows


def write_report(
    report_path: Path,
    output_path: Path,
    output_delimiter: str,
    unified_columns: List[str],
    source_stats: List[dict],
    source_to_column_map: Dict[str, Dict[str, str]],
    merged_rows: int,
) -> None:
    report_path.parent.mkdir(parents=True, exist_ok=True)
    total_source_rows = sum(item["rows"] for item in source_stats)

    lines: List[str] = []
    lines.append("# CSV Consolidatie Rapport")
    lines.append("")
    lines.append(f"- Outputbestand: `{output_path}`")
    lines.append(f"- Output delimiter: `{output_delimiter}`")
    lines.append(f"- Totaal bronbestanden: `{len(source_stats)}`")
    lines.append(f"- Totaal doelschema kolommen (excl. source_file): `{len(unified_columns)}`")
    lines.append(f"- Totaal bronrijen: `{total_source_rows}`")
    lines.append(f"- Totaal samengevoegde rijen: `{merged_rows}`")
    lines.append(f"- Validatie rijtelling: `{'OK' if merged_rows == total_source_rows else 'MISMATCH'}`")
    lines.append("")

    lines.append("## Bronbestand overzicht")
    lines.append("")
    lines.append("| Bestand | Encoding | Delimiter | Rijen |")
    lines.append("|---|---|---|---:|")
    for item in source_stats:
        delimiter_display = item["delimiter"].replace("|", "\\|")
        lines.append(
            f"| `{item['source_file']}` | `{item['encoding']}` | `{delimiter_display}` | {item['rows']} |"
        )

    lines.append("")
    lines.append("## Kolommapping per bestand")
    lines.append("")
    for source_file in sorted(source_to_column_map):
        lines.append(f"### `{source_file}`")
        lines.append("")
        mapping = source_to_column_map[source_file]
        if not mapping:
            lines.append("(Geen kolommen gevonden)")
            lines.append("")
            continue
        lines.append("| Bronkolom | Doelkolom |")
        lines.append("|---|---|")
        for src, dst in mapping.items():
            src_disp = str(src).replace("|", "\\|")
            dst_disp = str(dst).replace("|", "\\|")
            lines.append(f"| `{src_disp}` | `{dst_disp}` |")
        lines.append("")

    report_path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Combineer alle CSV-bestanden uit een .7z archive naar één overzichtelijk CSV-bestand."
    )
    parser.add_argument(
        "--archive",
        type=Path,
        default=Path("/tmp/workspace/Proowner7/Data-Migratie/data-export.7z"),
        help="Pad naar input .7z archive",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("/tmp/workspace/Proowner7/Data-Migratie/combined-data.csv"),
        help="Pad naar output CSV",
    )
    parser.add_argument(
        "--report",
        type=Path,
        default=Path("/tmp/workspace/Proowner7/Data-Migratie/combined-data-report.md"),
        help="Pad naar output rapport",
    )
    parser.add_argument(
        "--delimiter",
        default=";",
        help="Delimiter voor output CSV (standaard ';')",
    )
    parser.add_argument(
        "--password",
        default="",
        help="Wachtwoord van de .7z archive",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    if len(args.delimiter) != 1:
        raise ValueError("Delimiter moet precies 1 karakter zijn.")

    if not args.archive.exists():
        raise FileNotFoundError(f"Archive niet gevonden: {args.archive}")

    with tempfile.TemporaryDirectory(prefix="data_migratie_extract_") as temp_dir:
        extract_dir = Path(temp_dir)
        extract_archive(args.archive, args.password, extract_dir)

        csv_files = sorted(extract_dir.rglob("*.csv"))
        if not csv_files:
            raise RuntimeError("Geen CSV-bestanden gevonden in archive.")

        unified_columns, source_to_column_map, source_stats = build_source_metadata(csv_files)
        merged_rows = merge_csv_files(
            csv_files,
            args.output,
            args.delimiter,
            unified_columns,
            source_to_column_map,
        )

        write_report(
            args.report,
            args.output,
            args.delimiter,
            unified_columns,
            source_stats,
            source_to_column_map,
            merged_rows,
        )

    print(f"Klaar: {args.output}")
    print(f"Rapport: {args.report}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (RuntimeError, ValueError, FileNotFoundError) as exc:
        print(f"Fout: {exc}")
        raise SystemExit(1)
