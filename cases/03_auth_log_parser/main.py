ruta = "cases/03_auth_log_parser/data/auth_events.txt"
total_eventos = 0
total_fallos = 0

with open(ruta, "r", encoding="utf-8") as archivo:
    for linea in archivo:
        linea_limpia = linea.strip()
        timestamp, hostname, src_ip, username, result = linea_limpia.split("|")

        print(
            f"Timestamp: {timestamp}, "
            f"Hostname: {hostname}, "
            f"Source IP: {src_ip}, "
            f"Username: {username}, "
            f"Result: {result}"
        )

        total_eventos += 1
        if result == "failure":
            total_fallos += 1

print(f"Total events: {total_eventos}")
print(f"Failures: {total_fallos}")

