# Repeated failed-login source IPs

## Business problem

A Tier 1 analyst extracts source addresses associated with failed VPN logins.
Escalating every line would duplicate work, while ignoring recurrence would hide
addresses responsible for repeated failures.

## Operational objective

Preserve the original observations, identify addresses appearing more than
once, and report each recurring address only once.

## Solution approach

- Load the ordered source observations into a list.
- Count occurrences using list operations.
- Add an address to the recurring list only when it appears more than once and
  has not already been reported.
- Count distinct addresses that occur exactly once.

## Observable result

```text
Total failed-login lines: 22
Repeated IPs (appeared more than once): ['10.10.20.167', '10.10.50.52', '10.10.31.226', '10.10.70.18', '10.10.60.147', '10.10.60.215']
IPs that occurred only once: 2
```

## Operational limitations

Repeated calls to `list.count()` trade performance for clarity in this
foundation implementation. Later cases introduce data structures better suited
to larger datasets.

## Run

```powershell
python cases/04_repeated_source_ips/main.py
```

