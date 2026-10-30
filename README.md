# Smart Parking Dashboard – Northampton (PFD200 prototype)

A small Power BI prototype that shows how car park occupancy could be presented for three Northampton car parks: Mayorhold, Campbell Square and St John's. It was built as a coursework project for the PFD200 Professional Development module (FdSc Computing).

> **Prototype.** The report uses a nine-record dataset of illustrative values. It is not live data, it does not describe real car park use, and it must not be used for operational decisions.

## Project status

| Item | Status |
|---|---|
| First version of the report: bar chart, line chart and Status slicer | Built 28 October 2026 |
| Final report page: occupancy-rate card, total card, Status and Location slicers, titles, data labels, calendar-ordered day chart and warning banner | Built 29 October 2026 |
| Cleaning log and data record | Done 29 October 2026 |
| Test log (five checks) and independent script check | 5 of 5 passed on 29 October 2026 |
| Security awareness banner and briefing | Banner added to the report; briefing in `security/` |
| Evaluation of the awareness campaign | Proposed – not yet carried out |

## What the report shows

- **Occupied spaces by location** – which of the three car parks has the most occupied spaces.
- **Occupied spaces by day of week** – Monday, Friday and Saturday are the only days in the data, shown in calendar order.
- **Occupancy rate** card (occupied spaces ÷ capacity), a **Total occupied** card, and **Status** and **Location** slicers.
- A warning banner at the top of the page.

Each row of the data is one car park on one day, so the report is descriptive. It does not forecast, and it is not a real-time tracker.

## Data

- 9 records, 6 fields: `Parking_ID`, `Location`, `Capacity`, `Occupied_Spaces`, `Day_of_Week`, `Status`.
- Illustrative values; no personal or third-party data.
- Status rule: Bottleneck at 90% occupancy or above, High at 80–89%, Normal below 80%.
- Field definitions, coverage and limitations: [docs/data_record.md](docs/data_record.md).

## Requirements

- **Power BI Desktop** (free, Windows) to open `report/SMART_PARKING.pbix`.
- **Microsoft Excel** (optional) to view `data/PARKINGDATA.xlsx`.
- **Python 3** (optional, no extra packages) to run `scripts/verify_totals.py`.

## Opening the report

1. Download the repository (green **Code** button, then **Download ZIP**) or clone it:

   ```bash
   git clone https://github.com/costy81/pfd200-smart-parking-dashboard.git
   ```

2. Open `report/SMART_PARKING.pbix` in Power BI Desktop.
3. The `.pbix` file stores the path of the data file on the author's computer. If Power BI reports a data source error, point it at your copy of the data:
   **Home → Transform data → Data source settings → Change Source…**, browse to `data/PARKINGDATA.xlsx` in the folder you downloaded, then **Close & Apply**.
4. Optional: check the totals independently of Power BI:

   ```bash
   python scripts/verify_totals.py data/parkingdata.csv
   ```

## Repository structure

```
README.md                          this file
report/SMART_PARKING.pbix          the Power BI report
data/PARKINGDATA.xlsx              the nine-record dataset
data/parkingdata.csv               CSV copy used by the checking script
docs/data_record.md                fields, coverage, limitations
docs/cleaning_log.md               Power Query steps with before/after counts
docs/test_log.md                   expected vs actual results for five checks
security/banner_and_briefing.md    warning banner, user briefing, threat table
scripts/verify_totals.py           independent calculation of the expected totals
screenshots/                       report, data, Power Query, test and script screenshots
```

## Testing

Five manual checks compare what the report shows with values calculated separately from the source rows (total occupied spaces, totals by location, totals by day, the Status slicer, and the Location slicer with the occupancy rate). All five passed on 29 October 2026. `scripts/verify_totals.py` recalculates the same values from the CSV without using Power BI (`screenshots/09_python_verify_totals.png`). Expected values, steps and results are in [docs/test_log.md](docs/test_log.md).

## How this repository was built

This project, including the Power BI report, supporting files, documentation, testing materials and repository structure, was created by the author, Costel Boaca, as part of the PFD200 Professional Development coursework.

## Security awareness materials

A warning banner on the report page and a one-page user briefing are in [security/banner_and_briefing.md](security/banner_and_briefing.md), together with the threat table they respond to. The campaign has been **designed but not yet evaluated** with users.

## Known limitations

- Very small static dataset: nine records, three car parks, three days of the week (Monday, Friday, Saturday).
- No time-of-day data, and no data for Tuesday to Thursday or Sunday.
- Not live data; results cannot be generalised to real car park use.
- The two charts show sums of occupied spaces, which add occupancy across different days; the occupancy-rate card is the more meaningful measure.
- The cleaning checks ran on clean data, so they do not show how the process copes with messy real-world records.

## Author and licence

Coursework project by Costel Boaca for PFD200 Professional Development. No licence file is included, so all rights are reserved.
