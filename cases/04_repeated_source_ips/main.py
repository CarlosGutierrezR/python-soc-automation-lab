from pathlib import Path

data_path = Path(__file__).parent / "data" / "failed_login_ips.txt"
source_ips = []
repeated_ips = []
single_occurrence_count = 0

with data_path.open("r", encoding="utf-8") as file:
    for line in file:
        source_ip = line.strip()
        if not source_ip:
            continue

        source_ips.append(source_ip)

        if (
            source_ips.count(source_ip) > 1
            and source_ip not in repeated_ips
        ):
            repeated_ips.append(source_ip)

for source_ip in source_ips:
    if source_ips.count(source_ip) == 1:
        single_occurrence_count += 1

print(f"Total failed-login lines: {len(source_ips)}")
print(f"Repeated IPs (appeared more than once): {repeated_ips}")
print(f"IPs that occurred only once: {single_occurrence_count}")

