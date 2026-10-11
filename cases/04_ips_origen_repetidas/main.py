from pathlib import Path

ruta_datos = Path(__file__).parent / "data" / "failed_login_ips.txt"
ips_origen = []
ips_repetidas = []
cantidad_ips_una_vez = 0

with ruta_datos.open("r", encoding="utf-8") as archivo:
    for linea in archivo:
        ip_origen = linea.strip()
        if not ip_origen:
            continue

        ips_origen.append(ip_origen)

        if ips_origen.count(ip_origen) > 1 and ip_origen not in ips_repetidas:
            ips_repetidas.append(ip_origen)

for ip_origen in ips_origen:
    if ips_origen.count(ip_origen) == 1:
        cantidad_ips_una_vez += 1

print(f"Líneas totales de fallos: {len(ips_origen)}")
print(f"IP repetidas: {ips_repetidas}")
print(f"IP que aparecen una sola vez: {cantidad_ips_una_vez}")

