# Laboratorio de automatización SOC con Python

Utilidades prácticas en Python orientadas a tareas habituales de un Centro de
Operaciones de Seguridad. El repositorio avanza desde la representación y
clasificación de eventos hasta el análisis de logs, la ingeniería de detección,
la respuesta a incidentes y la automatización mantenible.

Todos los ejemplos utilizan datos sintéticos. No se incluyen credenciales de
producción, datos personales ni indicadores reales de terceros.

## Casos operativos

| Caso | Resultado empresarial | Capacidad de Python | Estado |
|---|---|---|---|
| [01](cases/01_resumen_evento_autenticacion/) | Convertir un evento de autenticación en un registro legible para el analista | Variables, cadenas y booleanos | Completado |
| [02](cases/02_clasificacion_fallos_cuenta/) | Priorizar fallos según el tipo de cuenta | Lógica condicional | Completado |
| [03](cases/03_analisis_logs_autenticacion/) | Procesar una exportación y cuantificar la actividad fallida | Archivos, bucles y contadores | Completado |
| [04](cases/04_ips_origen_repetidas/) | Reducir el ruido a direcciones de origen recurrentes | Listas y pertenencia | Completado |
| 05 | Agrupar actividad de autenticación por hostname | Diccionarios | En curso |

## Ejecución

Se recomienda Python 3.11 o posterior. Los casos actuales utilizan únicamente
la biblioteca estándar.

```powershell
python cases/01_resumen_evento_autenticacion/main.py
python cases/02_clasificacion_fallos_cuenta/main.py
python cases/03_analisis_logs_autenticacion/main.py
python cases/04_ips_origen_repetidas/main.py
```

Los casos 03 y 04 funcionan desde cualquier directorio porque resuelven sus
datasets a partir de la ubicación del propio script.

## Enfoque de ingeniería

- Partir de una pregunta SOC concreta.
- Utilizar la abstracción de Python más pequeña que resuelva el problema.
- Trabajar con entradas sintéticas y reproducibles.
- Validar resultados observables antes de incorporar un caso.
- Documentar limitaciones y oportunidades de endurecimiento.
- Incorporar manejo de errores, logging, pruebas, configuración y CLI conforme
  aumenta la complejidad.

## Estructura

```text
cases/                  Casos empresariales independientes
tests/                  Pruebas de regresión ejecutables localmente
.github/workflows/      Integración continua
PROCEDENCIA_DATOS.md    Procedencia y restricciones de los datos
```

Cada caso contiene su implementación, datos sintéticos cuando son necesarios,
instrucciones de ejecución, resultado observable y limitaciones operativas.

## Controles de calidad

```powershell
python -m unittest discover -s tests -v
```

La misma suite se ejecuta en GitHub Actions sobre varias versiones de Python.

## Licencia

El proyecto se publica bajo la [licencia MIT](LICENSE).

