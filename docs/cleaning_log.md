# Cleaning log

Power Query steps for the `PARKINGDATA` table (Applied Steps: Source, Navigation, Promoted Headers, Changed Type, Added Custom, Changed Type1). Date of cleaning: 29 October 2026. Report version: `SMART_PARKING.pbix`, last saved 29 October 2026, 5:47 PM.

| Step | Rule or action | Rows before | Rows after | Justification and result |
|---|---|---|---|---|
| 1 | Load the `PARKINGDATA` sheet from `PARKINGDATA.xlsx` (**Source**, **Navigation**). | – | 9 | Starting point; 9 rows. |
| 2 | Promote the first row to headers (**Promoted Headers**). | 9 | 9 | Gives the fields usable names. |
| 3 | Set data types (**Changed Type**): `Parking_ID`, `Capacity` and `Occupied_Spaces` as whole numbers; `Location`, `Day_of_Week` and `Status` as text. | 9 | 9 | Allows numeric totals and stops numbers being treated as text. |
| 4 | Check for duplicate `Parking_ID` values and duplicate rows. | 9 | 9 | Column distribution for `Parking_ID`: 9 distinct, 9 unique. No duplicates. |
| 5 | Check for blank values and errors in all columns. | 9 | 9 | Column quality: 100% valid, 0% error, 0% empty for all 7 columns. No blanks. |
| 6 | Check that `Occupied_Spaces` does not exceed `Capacity`. | 9 | 9 | `scripts/verify_totals.py` reports no rows with occupied above capacity (highest occupancy is 97.1%); see `screenshots/09_python_verify_totals.png`. |
| 7 | Add a `Day_Number` column (Monday = 1 … Sunday = 7) with a custom column, set it to whole number (**Added Custom**, **Changed Type1**), then sort `Day_of_Week` by it in the report. | 9 | 9 | Shows days in calendar order instead of ordering them by value. A first attempt with a DAX calculated column failed with a circular-dependency error when used as the sort column, so the column was created in Power Query instead. |
| 8 | Define the Status rule. | 9 | 9 | Bottleneck at 90% occupancy or above; High at 80–89%; Normal below 80%. See `docs/data_record.md`. |

No records were removed, so the count is nine before and after cleaning. Because the dataset was already clean, these checks show that the process works on this dataset; they do not show how it would cope with messy data.

A calculated column `Occupancy %` (occupied ÷ capacity, shown as a percentage) was also added in the report. It is not part of the source data.

## Data-quality checks used

The checks follow three dimensions of data quality (Wang and Strong, 1996): **completeness** (step 5), **consistency** (steps 3 and 4) and **accuracy** (step 6).

## Evidence

- `screenshots/03_powerquery_steps_quality.png` – Applied Steps, Column quality and Column distribution.
- `screenshots/04_column_distribution_checks.png` – enlarged view of the column profile (9 distinct, 9 unique for `Parking_ID`).
- `screenshots/02_data_view.png` – the final table with `Status`, `Occupancy %` and `Day_Number`.

## How to reproduce the checks

- **Duplicates / blanks:** in Power Query turn on **View → Column quality** and **Column distribution**.
- **Occupied above capacity:** run `python scripts/verify_totals.py data/parkingdata.csv`.
- **Day order:** **Add column → Custom column** named `Day_Number` with an `if … then … else if …` expression on `Day_of_Week`, set the type to whole number, then in the report select `Day_of_Week` and use **Column tools → Sort by column → Day_Number**.

## Reference

Wang, R.Y. and Strong, D.M. (1996) 'Beyond accuracy: what data quality means to data consumers', *Journal of Management Information Systems*, 12(4), pp. 5–33.
