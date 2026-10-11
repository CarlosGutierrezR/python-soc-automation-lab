# Clasificación de fallos por tipo de cuenta

## Problema empresarial

Los fallos de autenticación no tienen el mismo riesgo operativo. Un fallo en una
cuenta administrativa o de servicio requiere una atención diferente al error de
contraseña de un usuario estándar.

## Objetivo operativo

Clasificar cada intento por su resultado y, cuando falle, identificar el tipo de
cuenta según la convención de nombres de la organización.

## Enfoque de solución

- Separar resultados exitosos, fallidos y desconocidos.
- Identificar cuentas administrativas mediante el prefijo `adm_`.
- Identificar cuentas de servicio mediante el prefijo `svc_`.
- Tratar las demás identidades fallidas como usuarios estándar.
- Evitar decisiones hardcodeadas para un usuario concreto.

## Resultado observable

```text
mdominguez: success, no requiere acción
adm_sys01: FAILURE, cuenta administrativa - relevante
svc_backup: FAILURE, cuenta de servicio - relevante; no debería fallar interactivamente
rnunez: FAILURE, cuenta de usuario estándar
adm_netops: success, no requiere acción
```

## Limitaciones operativas

La clasificación depende de una convención de nombres documentada. En producción,
el tipo de identidad debería validarse contra un directorio autoritativo.

## Ejecución

```powershell
python cases/02_clasificacion_fallos_cuenta/main.py
```

