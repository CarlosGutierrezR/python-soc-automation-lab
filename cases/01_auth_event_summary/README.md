# Authentication event summary

## Scenario

Represent a single failed authentication event and produce a concise summary
for an analyst.

## Demonstrated behavior

- Stores the event fields using clear variables.
- Derives the success state as a boolean comparison.
- Produces a human-readable event summary.

## Run

```powershell
python cases/01_auth_event_summary/main.py
```

