import random
class Servicio:
    def __init__(self,id,nombre_del_cliente,tipo_de_servicio,importe):
        self.id = id 
        self.nombre = nombre_del_cliente
        self.ts = tipo_de_servicio
        self.importe = importe
        
    def __str__(self):
        return str(self.id) + " " + str(self.nombre) + " " + str(self.ts) + " " + str(self.importe)


def validar_entre(inf,sup,texto):
    n = int(input(texto))
    while inf > n > sup:
        n = int(input('ERROR' + texto))
    return n

def validar_mayor_que(sup,texto):
    n = int(input(texto))
    while sup > n:
        print('ERROR' + texto)
    return n

def cargar_arreglo(n):
    vector = []
    nombres = ['Mateo','Marcos','Lucas','Juan','Pedro','Pablo','Maria','Zacarias']
    for i in range(n):
        id = random.randint(1,1000)
        nombre_cliente = random.choice(nombres)
        tipo_de_servicio = random.randint(1,10)
        importe = random.randint(500,10000)
        servicio = Servicio(id,nombre_cliente,tipo_de_servicio,importe)
        vector.append(servicio)
    return vector
        
def ordenar_vector(v):
    for i in range(len(v) - 1):
        for j in range(i + 1, len(v)):
            if v[j].id > v[i].id:
                v[i], v[j] = v[j], v[i]

def mostrar_intervalo(inf,sup,v):
    for servicio in v:
        if inf <= servicio.importe <= sup:
            print(servicio)

def contar(v):
    vector_de_conteo = [0] * 10
    for i in range(len(v)):
        indice = v[i].ts - 1
        vector_de_conteo[indice] += 1
    return vector_de_conteo

def mostrar_vector(v):
    for i in range(len(v)):
        if v[i] != 0:
            print(v[i]) 
            
def buscar_cliente(nom,v):
    for servicio in v:
        if servicio.nombre == nom:
            servicio.importe += 2000
            print(servicio)
            break
    print('no se encontro')
    