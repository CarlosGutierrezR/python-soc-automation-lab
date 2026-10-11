# Repeated failed-login source IPs

## Scenario

Review an ordered list of failed-login source addresses and identify which
addresses occur more than once without duplicating them in the report.

## Demonstrated behavior

- Preserves the original observations in a list.
- Counts repeated values using list operations.
- Prevents duplicate entries in the repeated-address report.

## Run

```powershell
python cases/04_repeated_source_ips/main.py
```

