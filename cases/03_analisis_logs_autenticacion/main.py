from pathlib import Path

ruta_datos = Path(__file__).parent / "data" / "auth_events.txt"
total_eventos = 0
total_fallos = 0

with ruta_datos.open("r", encoding="utf-8") as archivo:
    for linea in archivo:
        linea_limpia = linea.strip()
        if not linea_limpia:
            continue

        fecha_hora, equipo, ip_origen, usuario, resultado = linea_limpia.split("|")

        print(
            f"Fecha: {fecha_hora}, "
            f"Equipo: {equipo}, "
            f"IP de origen: {ip_origen}, "
            f"Usuario: {usuario}, "
            f"Resultado: {resultado}"
        )

        total_eventos += 1
        if resultado == "failure":
            total_fallos += 1

print(f"Total de eventos: {total_eventos}")
print(f"Fallos: {total_fallos}")

