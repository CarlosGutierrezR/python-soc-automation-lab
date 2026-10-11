# Resumen de un evento de autenticación

## Problema empresarial

Un analista SOC recibe un evento de autenticación durante el relevo de turno.
Los campos deben representarse de forma consistente y convertirse en un registro
que otro analista pueda comprender sin interpretar valores sueltos.

## Objetivo operativo

Generar un resumen del evento y un booleano explícito que indique si el intento
de autenticación tuvo éxito.

## Enfoque de solución

- Representar fecha, identidad, endpoint, dirección de origen, método y resultado.
- Derivar el estado de éxito mediante una comparación booleana.
- Formatear el evento completo para su revisión.

## Resultado observable

```text
Fecha: 2024-03-10 21:47:00 Usuario: rnunez Equipo: WKSTN-SAL-004 IP de origen: 10.10.30.55 Método: password Resultado: failure
¿El intento tuvo éxito? False
```

## Limitaciones operativas

Este caso procesa un único evento en memoria. La lectura desde archivos, la
validación de esquemas y los valores malformados se incorporan posteriormente.

## Ejecución

```powershell
python cases/01_resumen_evento_autenticacion/main.py
```

