# Data Migratie CSV Consolidatie

Gebruik `merge_csv_from_7z.py` om alle CSV-bestanden uit een `.7z`-archive samen te voegen naar één overzichtelijk CSV-bestand.

## Voorbeeld

```bash
python /tmp/workspace/Proowner7/Data-Migratie/merge_csv_from_7z.py \
  --archive /tmp/workspace/Proowner7/Data-Migratie/data-export.7z \
  --output /tmp/workspace/Proowner7/Data-Migratie/combined-data.csv \
  --report /tmp/workspace/Proowner7/Data-Migratie/combined-data-report.md \
  --delimiter ';' \
  --password 'JOUW_7Z_WACHTWOORD'
```

## Wat het script doet

- pakt de `.7z` archive uit
- detecteert per CSV delimiter en encoding
- normaliseert kolomnamen naar een uniform doelschema
- voegt alle rijen samen in één output CSV
- voegt `source_file` toe voor herleidbaarheid
- maakt een rapport met kolommapping, rijtellingen en validatie

> Let op: de aangeleverde archive is versleuteld. Zonder correct wachtwoord kan de data niet worden uitgelezen.
