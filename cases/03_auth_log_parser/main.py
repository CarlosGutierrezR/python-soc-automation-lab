from pathlib import Path

data_path = Path(__file__).parent / "data" / "auth_events.txt"
total_events = 0
total_failures = 0

with data_path.open("r", encoding="utf-8") as file:
    for line in file:
        clean_line = line.strip()
        if not clean_line:
            continue

        timestamp, hostname, source_ip, username, result = clean_line.split("|")

        print(
            f"Timestamp: {timestamp}, "
            f"Hostname: {hostname}, "
            f"Source IP: {source_ip}, "
            f"Username: {username}, "
            f"Result: {result}"
        )

        total_events += 1
        if result == "failure":
            total_failures += 1

print(f"Total events: {total_events}")
print(f"Failures: {total_failures}")

