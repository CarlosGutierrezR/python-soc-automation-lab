# Authentication event summary

## Business problem

A SOC analyst receives an authentication record through a handover message. The
individual fields must be represented consistently and converted into a concise
record that another analyst can read without interpreting raw values.

## Operational objective

Produce a one-line event summary and an explicit boolean indicating whether the
attempt succeeded.

## Solution approach

- Represent timestamp, identity, endpoint, source address, method, and result as
  named values.
- Derive the success state from the authentication result.
- Format the complete event for analyst review.

## Observable result

```text
Fecha: 2024-03-10 21:47:00 Usuario: rnunez Equipo: WKSTN-SAL-004 IP de origen: 10.10.30.55 Metodo: password Resultado: failure
Was this attempt successful? False
```

## Operational limitations

This foundation case handles one in-memory event. File ingestion, schema
validation, and malformed values are introduced in later cases.

## Run

```powershell
python cases/01_auth_event_summary/main.py
```

