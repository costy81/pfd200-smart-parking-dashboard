# Security awareness materials

These materials respond to the threats in the table below. The campaign is **designed but not yet evaluated** with users.

## Threat table

| ID | Asset | Threat | Vulnerability | Mitigation | Residual or user-dependent risk |
|---|---|---|---|---|---|
| T1 | Dataset | Incorrect analysis | Missing or duplicate records. | Profile the data; validate types; document cleaning. | Remains. Users may still misinterpret limitations. |
| T2 | Report file | Unauthorised changes | File shared without access controls. | Restrict write access; keep versioned backups (GitHub history). | Remains. Authorised users may overwrite the file. |
| T3 | Source data | Licence breach | Unclear usage permissions. | Use aggregated, non-personal data and record the data source. | Low. The dataset is small, holds no personal data and has no third-party content. |
| T4 | Account | Account compromise | Weak password; unattended device. | Unique password, multi-factor authentication, screen lock. | Remains. A user may approve a fraudulent sign-in prompt. |
| T5 | Dashboard | Misleading decision | Old data appears current, or estimates are unclear. | Show source and date; label as illustrative, not live data; state limitations. | Remains. Viewers may ignore labels or use stale exports. |

## Audience and behavioural goals

**Audience:** council analysts and parking managers who view or share the report.

1. Check the data source and date before reusing figures externally (T5).
2. Share the report through the approved channel instead of sending raw exports by email or messaging (T2).
3. Report unexpected sign-in or multi-factor approval requests (T4).

## Banner text (top of the report page)

> **PROTOTYPE – NOT LIVE DATA.** These figures are illustrative and do not show current car park use. Do not use them for operational decisions. Before sharing, check the source and date, and share the report through the approved channel – not as an emailed export.

The banner is a text box across the top of the report page with a light red fill, so it is visible whenever the report is opened (`screenshots/01_final_report.png`).

## One-page user briefing

**Using the Smart Parking Dashboard safely**

- **What it is.** A prototype with nine illustrative records, to show how car park use could be presented. It is not live data.
- **Before you reuse a number.** Check the data source and date shown on the report, and label anything you share as illustrative.
- **Sharing.** Share the report through the approved channel (a shared workspace or the repository link). Do not send raw exports by email or personal messaging.
- **Sign-in prompts.** If you receive a sign-in or multi-factor approval request that you did not start, do not approve it. Report it to the report owner.
- **Questions.** Ask the report owner named in the repository README.

## Scenario questions for the proposed evaluation

| Scenario | Expected response | Result |
|---|---|---|
| A manager asks you to paste the Friday chart into a council report. What should you check and add? | Check the source and date; label the figures as illustrative. | Not yet tested |
| A colleague asks you to send the raw data file by personal messaging. What should you do? | Decline and point them to the approved channel or the repository. | Not yet tested |
| You receive a sign-in approval prompt that you did not start. What should you do? | Do not approve it; report it. | Not yet tested |

## Evaluation status

**Proposed – not yet carried out.** If you run it with real users (for example classmates), record the date, the number of participants and their answers here, and keep the wording in the README and in the portfolio consistent with what actually happened.
