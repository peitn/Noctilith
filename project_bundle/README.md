# Project bundle restore guide

This folder contains a chunked Base64 bundle of the uploaded Noctilith project.

## What is here

- `part_000.b64` ... `part_050.b64`
- split replacement for one filtered chunk:
  - `part_017a.b64`
  - `part_017b1.b64`
  - `part_017b2.b64`
- `rebuild_zip.py` — rebuilds the ZIP only
- `rebuild_and_extract.py` — rebuilds the ZIP and extracts it

## Rebuild ZIP only

```bash
python project_bundle/rebuild_zip.py
```

This creates:

- `project_bundle/noctilith2_restored.zip`

## Rebuild and extract

```bash
python project_bundle/rebuild_and_extract.py
```

This creates:

- `project_bundle/noctilith2_restored.zip`
- `project_bundle/restored_noctilith2/`

## Notes

- The rebuild script already knows that `part_017` was split into three files.
- If any chunk file is missing, the script will stop with a clear error.
