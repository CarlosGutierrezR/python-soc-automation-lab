ruta = "cases/04_repeated_source_ips/data/failed_login_ips.txt"
list_ips = []
ips_repeated = []
cant_ips_una_vez = 0

with open(ruta, "r", encoding="utf-8") as archivo:
    for linea in archivo:
        linea_limpia = linea.strip()
        list_ips.append(linea_limpia)

        if (
            list_ips.count(linea_limpia) > 1
            and linea_limpia not in ips_repeated
        ):
            ips_repeated.append(linea_limpia)

for ip in list_ips:
    if list_ips.count(ip) == 1:
        cant_ips_una_vez += 1

print(f"Total failed-login lines: {len(list_ips)}")
print(f"Repeated IPs (appeared more than once): {ips_repeated}")
print(f"IPs that occurred only once: {cant_ips_una_vez}")

