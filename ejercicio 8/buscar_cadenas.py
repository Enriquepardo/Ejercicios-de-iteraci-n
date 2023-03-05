
def descomponer_cadena():
    cadena = input("Introduce la cadena a descomponer: ")
    separador = input("Introduce el separador: ")
    
    partes = cadena.split(separador)
    
    tabla = []
    for i, parte in enumerate(partes):
        tabla.append([i+1, parte])
    
    return tabla

tabla = descomponer_cadena()

print("n.°\tCadena")
for fila in tabla:
    print(f"{fila[0]}\t{fila[1]}")


def buscar_campos_gcos():
    with open('/etc/passwd', 'r') as archivo:
        lineas = archivo.readlines()
    campos_gcos_incompletos = []
    for linea in lineas:
        campos = descomponer_cadena(linea, ':')
        if len(campos) >= 5 and campos[4][1] == '':
            campos_gcos_incompletos.append(campos[0][1])
    if campos_gcos_incompletos:
        print('Alerta: los siguientes usuarios tienen el campo GCOS incompleto:')
        for usuario in campos_gcos_incompletos:
            print(usuario)
    else:
        print('Todos los campos GCOS están completados.')


descomponer_cadena()



