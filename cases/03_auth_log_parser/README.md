# Authentication log parser

## Business problem

A previous SOC shift provides a pipe-delimited authentication export. Manually
reviewing individual lines does not provide a reliable event total or failure
count and does not scale when the export changes size.

## Operational objective

Process every record in the export, expose its relevant fields, and report the
total number of authentication events and failures.

## Solution approach

- Read the export sequentially instead of loading a fixed number of records.
- Remove line terminators before parsing.
- Split each event into its five documented fields.
- Maintain counters derived from observed records rather than hard-coded totals.

## Input format

```text
timestamp|hostname|src_ip|username|result
```

## Observable result

The supplied synthetic dataset produces:

```text
Total events: 18
Failures: 4
```

## Operational limitations

This version expects every non-empty record to contain exactly five fields.
Malformed-row handling, structured logging, and reusable functions are added as
the project advances.

## Run

```powershell
python cases/03_auth_log_parser/main.py
```

