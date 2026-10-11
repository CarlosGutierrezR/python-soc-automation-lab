# Python SOC Automation Lab

Practical Python utilities built around recurring Security Operations Center
workflows. The repository grows incrementally from event representation and
classification to log parsing, aggregation, detection engineering, incident
response, and maintainable security automation.

All examples use synthetic data. No production credentials, personal data, or
real third-party indicators are included.

## Operational case studies

| Case | Business outcome | Python capability | Status |
|---|---|---|---|
| [01](cases/01_auth_event_summary/) | Convert a raw authentication event into an analyst-readable record | Variables, strings, booleans | Complete |
| [02](cases/02_account_failure_classification/) | Prioritize failures according to account type | Conditional logic | Complete |
| [03](cases/03_auth_log_parser/) | Process an authentication export and quantify failed activity | Files, loops, counters | Complete |
| [04](cases/04_repeated_source_ips/) | Reduce failed-login noise to recurring source addresses | Lists and membership checks | Complete |
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

Each directory contains a focused implementation, synthetic input data when
needed, execution instructions, an observable result, and documented operational
limitations. Completed cases are committed independently so the history shows
how the project evolves over time.

