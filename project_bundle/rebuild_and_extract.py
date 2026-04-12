#!/usr/bin/env python3
from __future__ import annotations

import shutil
import zipfile
from pathlib import Path

from rebuild_zip import rebuild


def extract(
    bundle_dir: Path,
    zip_name: str = 'noctilith2_restored.zip',
    extract_dir_name: str = 'restored_noctilith2'
) -> Path:
    zip_path = bundle_dir / zip_name
    if not zip_path.is_file():
        zip_path = rebuild(bundle_dir, zip_name)

    extract_dir = bundle_dir / extract_dir_name
    if extract_dir.exists():
        shutil.rmtree(extract_dir)
    extract_dir.mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(zip_path, 'r') as zf:
        zf.extractall(extract_dir)

    return extract_dir


if __name__ == '__main__':
    bundle_dir = Path(__file__).resolve().parent
    zip_path = rebuild(bundle_dir)
    out_dir = extract(bundle_dir)
    print(f'Restored ZIP: {zip_path}')
    print(f'Extracted to: {out_dir}')
