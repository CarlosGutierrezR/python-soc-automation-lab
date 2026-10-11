eventos = [
    {"usuario": "mdominguez", "resultado": "success"},
    {"usuario": "adm_sys01", "resultado": "failure"},
    {"usuario": "svc_backup", "resultado": "failure"},
    {"usuario": "rnunez", "resultado": "failure"},
    {"usuario": "adm_netops", "resultado": "success"},
]

for evento in eventos:
    usuario = evento["usuario"]
    resultado = evento["resultado"]

    if resultado == "success":
        print(f"{usuario}: {resultado}, no requiere acción")
    elif resultado == "failure":
        if usuario.startswith("adm_"):
            print(f"{usuario}: {resultado.upper()}, cuenta administrativa - relevante")
        elif usuario.startswith("svc_"):
            print(
                f"{usuario}: {resultado.upper()}, cuenta de servicio - relevante; "
                "no debería fallar interactivamente"
            )
        else:
            print(f"{usuario}: {resultado.upper()}, cuenta de usuario estándar")
    else:
        print(f"{usuario}: {resultado.upper()}, resultado de autenticación desconocido")

