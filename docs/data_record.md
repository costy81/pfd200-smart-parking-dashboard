# Data record

| Item | Detail |
|---|---|
| Dataset name | PARKINGDATA (Excel sheet loaded into Power BI as the table `PARKINGDATA`) |
| Records and fields | 9 records, 6 fields |
| Coverage | Three car parks (Mayorhold, Campbell Square, St John's) and three days of the week (Monday, Friday, Saturday); one record per car park per day. No time-of-day data. |
| Source and licence | Illustrative values created for this project. The dataset holds no personal or third-party data, so no licence restrictions apply. |
| Personal data | None. |

## Field definitions

| Field | Type | Definition |
|---|---|---|
| `Parking_ID` | Whole number | Unique record identifier (1–9). |
| `Location` | Text | Car park name: Mayorhold, Campbell Square or St John's. |
| `Capacity` | Whole number | Number of spaces at the car park (450 Campbell Square, 350 St John's, 600 Mayorhold). |
| `Occupied_Spaces` | Whole number | Spaces occupied in the record. |
| `Day_of_Week` | Text | Friday, Saturday or Monday. |
| `Status` | Text | Normal, High or Bottleneck. Rule: Bottleneck at 90% occupancy or above, High at 80–89%, Normal below 80% (see `docs/cleaning_log.md`, step 8). |

Two further columns are added inside the report: `Day_Number` (Power Query custom column, used to sort the days) and `Occupancy %` (calculated column, occupied ÷ capacity).

## Limitations

- Very small static dataset; results cannot be generalised to real car park use.
- Three days of the week only (no Tuesday to Thursday or Sunday).
- Not live data.
- The Status labels are stored as text, so their rule is documented here rather than in the data.
