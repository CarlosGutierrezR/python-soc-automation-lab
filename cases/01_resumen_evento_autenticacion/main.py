fecha_hora = "2024-03-10 21:47:00"
usuario = "rnunez"
equipo = "WKSTN-SAL-004"
ip_origen = "10.10.30.55"
metodo_autenticacion = "password"
resultado = "failure"

exitoso = resultado == "success"

print(
    f"Fecha: {fecha_hora} Usuario: {usuario} Equipo: {equipo} "
    f"IP de origen: {ip_origen} Método: {metodo_autenticacion} "
    f"Resultado: {resultado}"
)
print(f"¿El intento tuvo éxito? {exitoso}")

