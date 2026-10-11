# Account failure classification

## Business problem

Authentication failures do not carry the same operational risk. A failed login
for an administrative or service account warrants different analyst attention
from a standard user entering an incorrect password.

## Operational objective

Classify each authentication attempt by result and, for failures, identify the
account category from the organization's naming convention.

## Solution approach

- Evaluate successful, failed, and unknown outcomes separately.
- Identify administrative accounts through the `adm_` prefix.
- Identify service accounts through the `svc_` prefix.
- Treat remaining failed identities as standard user accounts.
- Avoid hard-coded decisions tied to one specific username.

## Observable result

```text
mdominguez: success, no action needed
adm_sys01: FAILURE, admin account - notable
svc_backup: FAILURE, service account - notable; service accounts should not fail interactively
rnunez: FAILURE, standard user account
adm_netops: success, no action needed
```

## Operational limitations

The account categories depend on a documented naming convention. A production
implementation should validate results and obtain identity type from an
authoritative directory when available.

## Run

```powershell
python cases/02_account_failure_classification/main.py
```

