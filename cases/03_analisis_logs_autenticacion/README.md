# Análisis de logs de autenticación

## Problema empresarial

El turno anterior entrega una exportación de autenticaciones delimitada por `|`.
La revisión manual no ofrece totales fiables ni escala cuando cambia el tamaño.

## Objetivo operativo

Procesar todos los registros, mostrar sus campos relevantes y calcular la
cantidad total de eventos y fallos.

## Formato de entrada

```text
timestamp|hostname|src_ip|username|result
```

## Enfoque de solución

- Resolver el dataset desde la ubicación del script.
- Leer secuencialmente sin depender de una cantidad fija de registros.
- Ignorar líneas vacías y retirar terminadores antes del análisis.
- Separar cada evento en sus cinco campos documentados.
- Calcular contadores a partir de los registros observados.

## Resultado observable

```text
Total de eventos: 18
Fallos: 4
```

## Limitaciones operativas

Cada línea no vacía debe contener exactamente cinco campos. La validación de
filas malformadas y el logging estructurado se incorporarán posteriormente.

## Ejecución

```powershell
python cases/03_analisis_logs_autenticacion/main.py
```

