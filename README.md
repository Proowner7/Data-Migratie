# Debiteuren automatische update

Dit project bevat een script om een debiteuren-export uit Exact Online te vergelijken met je werkbestand en automatisch alleen nieuwe debiteuren toe te voegen.

## Installatie

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Gebruik

```bash
python debtor_sync.py \
  --source /pad/naar/exact-export.xlsx \
  --workbook /pad/naar/werkbestand.xlsx \
  --output-dir /pad/naar/output \
  --key-columns "Debiteurnummer,KvK,Relatiecode" \
  --required-work-columns "Debiteurnummer,Naam"
```

## Wat het script doet

1. Leest bronbestand (Exact export) en werkbestand in (.xlsx/.xlsm/.csv).
2. Normaliseert waardes voor vergelijking (spaties verwijderen, case-insensitive vergelijking).
3. Vergelijkt op sleutelkolommen in prioriteitsvolgorde (eerste niet-lege sleutel wint).
4. Voegt alleen nieuwe debiteuren toe aan het outputbestand.
5. Laat bestaande records ongemoeid, maar markeert afwijkingen als conflict.
6. Maakt per run een outputmap met timestamp:
   - `debiteuren-updated.xlsx` (bijgewerkt bestand)
   - `report.json` (aantallen en run-informatie)
   - `conflicts.csv` (dubbele records, conflicten, lege sleutel)

## Validatie en foutafhandeling

- Fout bij ontbrekende sleutelkolommen tussen bron en werkbestand.
- Fout bij ontbrekende verplichte kolommen in het werkbestand.
- Fout bij niet-ondersteund bestandstype.
- Bronregels zonder sleutel worden gelogd in `conflicts.csv`.

## Testen

```bash
pytest -q
```
