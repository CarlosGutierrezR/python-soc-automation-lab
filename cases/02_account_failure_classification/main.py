events = [
    {
        "username": "mdominguez",
        "result": "success",
    },
    {
        "username": "adm_sys01",
        "result": "failure",
    },
    {
        "username": "svc_backup",
        "result": "failure",
    },
    {
        "username": "rnunez",
        "result": "failure",
    },
    {
        "username": "adm_netops",
        "result": "success",
    },
]

for event in events:
    username = event["username"]
    result = event["result"]

    if result == "success":
        print(f"{username}: {result}, no action needed")
    elif result == "failure":
        if username.startswith("adm_"):
            print(f"{username}: {result.upper()}, admin account - notable")
        elif username.startswith("svc_"):
            print(
                f"{username}: {result.upper()}, service account - notable; "
                "service accounts should not fail interactively"
            )
        else:
            print(f"{username}: {result.upper()}, standard user account")
    else:
        print(f"{username}: {result.upper()}, unknown authentication result")

