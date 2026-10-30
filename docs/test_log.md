# Test log

Manual checks that compare what the report shows with values calculated separately from the nine source rows. The expected values were worked out from the data with `python scripts/verify_totals.py data/parkingdata.csv`, which does not use Power BI.

- **Version tested:** `SMART_PARKING.pbix`, last saved 29 October 2026, 5:47 PM
- **Date:** 29 October 2026
- **Tool:** Power BI Desktop 2.159.883.0 (Windows)
- **Independent check:** `python scripts/verify_totals.py data/parkingdata.csv` (screenshot `screenshots/09_python_verify_totals.png`)

## Results

| ID | Check | Expected result | Actual | Pass / fail | Date |
|---|---|---|---|---|---|
| T1 | Total occupied spaces, all records. | 3,130 | Total Occupied card shows 3,130 | Pass | 29 Oct 2026 |
| T2 | Occupied spaces by location (bar chart). | Mayorhold 1,310; Campbell Square 1,020; St John's 800. | Data labels show 1310, 1020 and 800 | Pass | 29 Oct 2026 |
| T3 | Occupied spaces by day, in calendar order. | Monday 580; Friday 1,340; Saturday 1,210. | Days appear in the order Monday, Friday, Saturday with labels 580, 1340, 1210 | Pass | 29 Oct 2026 |
| T4 | Status slicer set to Bottleneck. | Only Bottleneck records shown: Mayorhold 580, Campbell Square 420, St John's 340, total 1,340 (Friday only). | Bars show 580, 420, 340; the line chart shows Friday only (1340); the cards show 95.7% and 1,340 | Pass | 29 Oct 2026 |
| T5 | Location slicer set to Mayorhold; occupancy-rate card. | Mayorhold: 1,310 of 1,800 spaces = 72.8%. All locations: 3,130 of 4,200 = 74.5%. | With Mayorhold selected the cards show 72.8% and 1,310; with no selection the rate card shows 74.5% | Pass | 29 Oct 2026 |

Evidence: `screenshots/05_T1-T3_unfiltered.png` (T1–T3 and the 74.5% overall rate), `screenshots/06_T4_bottleneck.png` (T4), `screenshots/07_T5_mayorhold.png` (T5) and `screenshots/09_python_verify_totals.png` (independent recalculation of all expected values).

## How each check was run

1. **T1** – With no slicer selected, read the Total Occupied card and compare it with 3,130.
2. **T2** – Read the data labels on the bar chart and compare them with the three expected totals.
3. **T3** – Read the line chart labels and confirm the days appear in calendar order (Monday, Friday, Saturday), not sorted by value.
4. **T4** – Select **Bottleneck** in the Status slicer and compare the charts and cards with the expected records, then clear the slicer.
5. **T5** – Select **Mayorhold** in the Location slicer and read the occupancy-rate card, then clear the slicer and read the overall rate. The measures are:

   ```
   Occupancy Rate = DIVIDE(SUM(PARKINGDATA[Occupied_Spaces]), SUM(PARKINGDATA[Capacity]))
   Total Occupied = FORMAT(SUM(PARKINGDATA[Occupied_Spaces]), "#,0")
   ```

## Failures and retests

No check failed. One build problem was fixed along the way: sorting `Day_of_Week` by a DAX calculated column gave a circular-dependency error, so the `Day_Number` column was created in Power Query instead (see `docs/cleaning_log.md`, step 7).

## Notes

- The expected values come from only nine records, so the checks test arithmetic and filtering, not how the report behaves on larger or messier data.
- The Total Occupied card uses a text measure (`FORMAT`) so that it shows 3,130 instead of the abbreviated "3K". It is for display only; the charts use the numeric `Occupied_Spaces` field.
- The Status labels follow the rule in `docs/data_record.md`, so T4 tests that the slicer filters correctly, not that the labels match an independent source.
