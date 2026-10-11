datos = [
    {
        "Usuario": "mdominguez",
        "Tipo_de_evento": "interactive_logon",
        "Resultado": "success",
    },
    {
        "Usuario": "adm_sys01",
        "Tipo_de_evento": "admin_logon",
        "Resultado": "failure",
    },
    {
        "Usuario": "svc_backup",
        "Tipo_de_evento": "service_logon",
        "Resultado": "failure",
    },
    {
        "Usuario": "rnunez",
        "Tipo_de_evento": "interactive_logon",
        "Resultado": "failure",
    },
    {
        "Usuario": "adm_netops",
        "Tipo_de_evento": "admin_logon",
        "Resultado": "success",
    },
]

for dato in datos:
    usuario = dato["Usuario"]
    resultado = dato["Resultado"]

    if resultado == "success":
        print(f"{usuario}: {resultado}, no action needed")
    elif resultado == "failure":
        if usuario.startswith("adm_"):
            print(f"{usuario}: {resultado.upper()}, admin account - notable")
        elif usuario.startswith("svc_"):
            print(
                f"{usuario}: {resultado.upper()}, service account - notable; "
                "service accounts should not fail interactively"
            )
        else:
            print(f"{usuario}: {resultado.upper()}, standard user account")
    else:
        print(f"{usuario}: {resultado.upper()}, unknown authentication result")

