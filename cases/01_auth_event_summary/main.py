fecha = "2024-03-10 21:47:00"
usuario = "rnunez"
equipo = "WKSTN-SAL-004"
ip_origen = "10.10.30.55"
metodo = "password"
resultado = "failure"

attempt = resultado == "success"

print(
    f"Fecha: {fecha} Usuario: {usuario} Equipo: {equipo} "
    f"IP de origen: {ip_origen} Metodo: {metodo} Resultado: {resultado}"
)
print(f"Was this attempt successful? {attempt}")

