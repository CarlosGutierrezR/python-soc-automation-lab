# Account failure classification

## Scenario

Classify authentication outcomes and distinguish failed activity involving
administrative, service, and standard user accounts.

## Demonstrated behavior

- Evaluates successful, failed, and unknown outcomes separately.
- Uses account prefixes instead of hard-coded identities.
- Applies nested conditional logic to separate result and account type.

## Run

```powershell
python cases/02_account_failure_classification/main.py
```

