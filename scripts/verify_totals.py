#!/usr/bin/env python3
"""Independent check of the expected values used in docs/test_log.md.

Reads the parking data from a CSV file and prints:
  * data-quality checks (duplicates, blanks, occupied spaces above capacity);
  * total occupied spaces and capacity, and the overall occupancy rate;
  * totals and occupancy rate by location and by day of week (calendar order);
  * totals for each Status value, if the file has a Status column.

It does not use Power BI, so the figures can be compared with the report.

Usage:
    python scripts/verify_totals.py data/parkingdata.csv

Expected columns: Parking_ID, Location, Capacity, Occupied_Spaces, Day_of_Week
(optional: Status). Export the Excel table to CSV first (File > Save As > CSV).
"""
import csv
import sys
from collections import defaultdict

REQUIRED = ["Parking_ID", "Location", "Capacity", "Occupied_Spaces", "Day_of_Week"]
DAY_ORDER = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def load(path):
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        missing = [c for c in REQUIRED if c not in (reader.fieldnames or [])]
        if missing:
            sys.exit(f"Missing column(s): {', '.join(missing)}. Found: {reader.fieldnames}")
        return reader.fieldnames, list(reader)


def rate(occupied, capacity):
    return f"{100 * occupied / capacity:.1f}%" if capacity else "n/a"


def main(path):
    fields, rows = load(path)
    print(f"File: {path}")
    print(f"Rows: {len(rows)}   Columns: {len(fields)}\n")

    print("Data-quality checks")
    ids = [r["Parking_ID"] for r in rows]
    dup_ids = sorted({i for i in ids if ids.count(i) > 1})
    full_rows = [tuple(r[c] for c in fields) for r in rows]
    dup_rows = len(full_rows) - len(set(full_rows))
    blanks = [(n + 1, c) for n, r in enumerate(rows) for c in fields if not (r[c] or "").strip()]
    bad_numbers = []
    over = []
    for n, r in enumerate(rows, start=1):
        try:
            cap, occ = int(r["Capacity"]), int(r["Occupied_Spaces"])
        except ValueError:
            bad_numbers.append(n)
            continue
        if occ > cap:
            over.append(n)
    print(f"  Duplicate Parking_ID values : {dup_ids or 'none'}")
    print(f"  Duplicate rows              : {dup_rows or 'none'}")
    print(f"  Blank values (row, column)  : {blanks or 'none'}")
    print(f"  Non-numeric Capacity/Occupied rows: {bad_numbers or 'none'}")
    print(f"  Rows with Occupied > Capacity: {over or 'none'}\n")
    if bad_numbers:
        sys.exit("Fix the non-numeric rows before the totals can be calculated.")

    data = [
        {**r, "Capacity": int(r["Capacity"]), "Occupied_Spaces": int(r["Occupied_Spaces"])}
        for r in rows
    ]
    total_occ = sum(r["Occupied_Spaces"] for r in data)
    total_cap = sum(r["Capacity"] for r in data)
    print("Totals")
    print(f"  Total occupied spaces: {total_occ:,}")
    print(f"  Total capacity       : {total_cap:,}")
    print(f"  Occupancy rate       : {rate(total_occ, total_cap)}\n")

    by_loc = defaultdict(lambda: [0, 0])
    by_day = defaultdict(lambda: [0, 0])
    by_status = defaultdict(lambda: [0, 0])
    for r in data:
        for bucket, key in ((by_loc, r["Location"]), (by_day, r["Day_of_Week"])):
            bucket[key][0] += r["Occupied_Spaces"]
            bucket[key][1] += r["Capacity"]
        if "Status" in r:
            by_status[r["Status"]][0] += r["Occupied_Spaces"]
            by_status[r["Status"]][1] += r["Capacity"]

    def show(title, bucket, order=None):
        print(title)
        keys = sorted(bucket, key=order) if order else sorted(bucket)
        for k in keys:
            occ, cap = bucket[k]
            print(f"  {k:<18} occupied {occ:>6,}   capacity {cap:>6,}   rate {rate(occ, cap)}")
        print()

    show("By location", by_loc, order=str.lower)
    show(
        "By day of week (calendar order)",
        by_day,
        order=lambda d: DAY_ORDER.index(d.title()) if d.title() in DAY_ORDER else 99,
    )
    if by_status:
        show("By Status (what the Status slicer should show)", by_status)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
