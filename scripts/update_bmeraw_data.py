#!/usr/bin/env python3
"""
Usage: python scripts/update_bmeraw.py <input_file> [output_file]

Reads a .bmerawdata (JSON) file, updates `rawDataHeader.dateCreated` and
`rawDataHeader.dateCreated_ISO` to the current time, and recalculates the
4th column (index 3) in every row of `rawDataBody.dataBlock` as:

    epoch_at_start + (time_since_poweron / 1000)

where `time_since_poweron` is the 3rd column (index 2) in milliseconds.
The script writes the modified JSON to `output_file` or to
`<input_file>_updated.bmerawdata` by default.
"""
from __future__ import annotations

import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def save_json(obj: Any, path: Path) -> None:
    with path.open("w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, ensure_ascii=False)


def update_file(input_path: Path, output_path: Path) -> None:
    data = load_json(input_path)

    now_epoch = int(time.time())
    now_iso = datetime.now(timezone.utc).isoformat()

    # Update header
    raw_header = data.setdefault("rawDataHeader", {})
    raw_header["dateCreated"] = str(now_epoch)
    raw_header["dateCreated_ISO"] = now_iso

    # Use epoch_at_start = the (new) dateCreated as integer seconds
    try:
        epoch_at_start = int(raw_header["dateCreated"])
    except Exception:
        epoch_at_start = now_epoch

    # Update dataBlock
    raw_body = data.setdefault("rawDataBody", {})
    data_block = raw_body.get("dataBlock", [])

    for i, row in enumerate(data_block):
        if not isinstance(row, list):
            continue
        if len(row) <= 3:
            continue

        # time since power on is column index 2 (milliseconds)
        timesince = row[2]
        try:
            timesince_ms = float(timesince)
        except Exception:
            # leave unchanged if unparsable
            continue

        new_epoch = epoch_at_start + (timesince_ms / 1000.0)
        # store as integer seconds (match existing file style)
        row[3] = int(round(new_epoch))

    save_json(data, output_path)


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("Usage: update_bmeraw.py <input_file> [output_file]")
        return 2

    input_path = Path(argv[1])
    if not input_path.exists():
        print(f"Input file not found: {input_path}")
        return 3

    if len(argv) >= 3:
        output_path = Path(argv[2])
    else:
        output_path = input_path.with_name(input_path.stem + "_updated" + input_path.suffix)

    update_file(input_path, output_path)
    print(f"Wrote updated file to: {output_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
