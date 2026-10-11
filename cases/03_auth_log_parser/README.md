# Authentication log parser

## Scenario

Process a pipe-delimited authentication export, print every parsed event, and
report total activity and failed attempts.

## Input format

```text
timestamp|hostname|src_ip|username|result
```

## Run

```powershell
python cases/03_auth_log_parser/main.py
```

