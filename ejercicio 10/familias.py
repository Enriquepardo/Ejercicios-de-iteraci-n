import random

# Definición del tipo PERSONA
class PERSONA:
    def __init__(self, nombre, apellido, edad, padre=None, madre=None):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.padre = padre
        self.madre = madre

# Definición de las constantes
BORRADO = -1
VACIO = -2
HUERFANO = -3

# Inicialización de la tabla familias
familias = [None] * 1000
for i in range(1000):
    if random.random() < 0.8:
        nombre = f"Persona {i+1}"
        apellido = f"Apellido {i+1}"
        edad = random.randint(1, 50)
        padre = random.randint(0, 999)
        madre = random.randint(0, 999)
        familias[i] = PERSONA(nombre, apellido, edad, padre, madre)
    else:
        familias[i] = BORRADO

# Función para obtener la lista de todas las personas registradas con una edad de 20 a 30 años
def personas_20_30():
    personas = []
    for persona in familias:
        if persona is not None and persona != BORRADO and PERSONA.edad >= 20 and PERSONA.edad <= 30:
            personas.append(persona)
    return personas

# Función para envejecer 1 año a todas las personas registradas
def envejecer():
    for i in range(len(familias)):
        if familias[i] is not None and familias[i] != BORRADO:
            familias[i].edad += 1

# Función para establecer la lista de todos los huérfanos de menos de 15 años
def huerfanos():
    huerfanos = []
    for i in range(len(familias)):
        if familias[i] is not None and familias[i] != BORRADO:
            if (familias[i].padre is None or familias[familias[i].padre] == BORRADO) and (familias[i].madre is None or familias[familias[i].madre] == BORRADO) and familias[i].edad < 15:
                huerfanos.append(familias[i])
    return huerfanos

# Función para determinar la identidad del padre de 'Jaime MARTÍN'
def padre_jaime():
    for i in range(len(familias)):
        if familias[i] is not None and familias[i] != BORRADO and familias[i].nombre == 'Jaime' and familias[i].apellido == 'MARTÍN':
            if familias[i].padre is None:
                return None
            else:
                return familias[familias[i].padre].nombre + ' ' + familias[familias[i].padre].apellido

# Función para establecer la lista de los hermanos y hermanas de 'Jaime MARTÍN'
def hermanos_jaime():
    hermanos = []
    jaime_padre = None
    # Buscar a Jaime MARTÍN y obtener su padre (si tiene)
    for i in range(len(familias)):
        if familias[i] is not None and familias[i] != BORRADO and familias[i].apellido == 'MARTÍN' and familias[i].nombre == 'Jaime':
            if familias[i].padre is not None and familias[i].padre != HUERFANO and familias[i].padre != BORRADO:
                jaime_padre = familias[i].padre
            break
    # Buscar a los hermanos de Jaime MARTÍN (si tiene padre)
    if jaime_padre is not None:
        for i in range(len(familias)):
            if familias[i] is not None and familias[i] != BORRADO and familias[i].padre == jaime_padre and familias[i] != jaime_padre:
                hermanos.append(familias[i])
    return hermanos





