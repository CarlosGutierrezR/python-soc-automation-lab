# Python SOC Automation Lab

Practical Python utilities built around recurring Security Operations Center
workflows. The repository grows incrementally from event representation and
classification to log parsing, aggregation, detection engineering, incident
response, and maintainable security automation.

All examples use synthetic data. No production credentials, personal data, or
real third-party indicators are included.

## Current cases

| Case | SOC task | Python focus | Status |
|---|---|---|---|
| 01 | Summarize an authentication event | Variables, strings, booleans | Complete |
| 02 | Classify authentication failures by account type | Conditional logic | Complete |
| 03 | Parse an authentication export and count failures | Files, loops, counters | Complete |
| 04 | Identify repeated failed-login source IPs | Lists and membership checks | Complete |
| 05 | Aggregate authentication activity by hostname | Dictionaries | In progress |

## Run a case

Python 3.11 or later is recommended. The current cases use only the Python
standard library.

From the repository root:

```powershell
python cases/01_auth_event_summary/main.py
python cases/02_account_failure_classification/main.py
python cases/03_auth_log_parser/main.py
python cases/04_repeated_source_ips/main.py
```

## Engineering approach

- Start from a concrete SOC question.
- Use the smallest suitable Python abstraction.
- Keep inputs synthetic and reproducible.
- Validate observable results before committing a case.
- Add error handling, logging, tests, configuration, and CLI interfaces as the
  project advances.

## Repository structure

```text
cases/
  01_auth_event_summary/
  02_account_failure_classification/
  03_auth_log_parser/
  04_repeated_source_ips/
```

Each directory contains a focused implementation and a short case description.

