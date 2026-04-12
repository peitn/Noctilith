#!/usr/bin/env python3
from __future__ import annotations

import base64
from pathlib import Path


def ordered_parts() -> list[str]:
    parts: list[str] = []
    for i in range(51):
        if i == 17:
            parts.extend([
                'part_017a.b64',
                'part_017b1.b64',
                'part_017b2.b64',
            ])
        else:
            parts.append(f'part_{i:03d}.b64')
    return parts


def rebuild(bundle_dir: Path, output_name: str = 'noctilith2_restored.zip') -> Path:
    pieces: list[str] = []
    missing: list[str] = []

    for name in ordered_parts():
        path = bundle_dir / name
        if not path.is_file():
            missing.append(name)
            continue
        pieces.append(path.read_text(encoding='utf-8').strip())

    if missing:
        raise FileNotFoundError(
            'Missing chunk files: ' + ', '.join(missing)
        )

    joined = ''.join(pieces)
    raw = base64.b64decode(joined)

    out_path = bundle_dir / output_name
    out_path.write_bytes(raw)
    return out_path


if __name__ == '__main__':
    bundle_dir = Path(__file__).resolve().parent
    out = rebuild(bundle_dir)
    print(f'Restored ZIP: {out}')
