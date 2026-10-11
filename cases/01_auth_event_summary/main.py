timestamp = "2024-03-10 21:47:00"
username = "rnunez"
hostname = "WKSTN-SAL-004"
source_ip = "10.10.30.55"
auth_method = "password"
result = "failure"

successful = result == "success"

print(
    f"Timestamp: {timestamp} Username: {username} Hostname: {hostname} "
    f"Source IP: {source_ip} Method: {auth_method} Result: {result}"
)
print(f"Was this attempt successful? {successful}")

