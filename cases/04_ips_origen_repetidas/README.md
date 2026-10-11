# Direcciones IP repetidas en fallos de autenticación

## Problema empresarial

Un analista Tier 1 extrae direcciones de origen asociadas con fallos de VPN.
Escalar todas las líneas duplicaría trabajo, mientras que ignorar la recurrencia
ocultaría los orígenes responsables de múltiples fallos.

## Objetivo operativo

Conservar las observaciones, identificar las direcciones que aparecen más de una
vez e informar cada dirección recurrente una sola vez.

## Enfoque de solución

- Resolver el dataset desde la ubicación del script.
- Ignorar líneas vacías para no tratarlas como direcciones.
- Conservar las observaciones ordenadas en una lista.
- Añadir una dirección solo cuando se repite y aún no fue informada.
- Contar las direcciones que aparecen exactamente una vez.

## Resultado observable

```text
Líneas totales de fallos: 22
IP repetidas: ['10.10.20.167', '10.10.50.52', '10.10.31.226', '10.10.70.18', '10.10.60.147', '10.10.60.215']
IP que aparecen una sola vez: 2
```

## Limitaciones operativas

Las llamadas repetidas a `list.count()` priorizan la claridad frente al
rendimiento. Casos posteriores incorporarán estructuras adecuadas para datasets
de mayor volumen.

## Ejecución

```powershell
python cases/04_ips_origen_repetidas/main.py
```

