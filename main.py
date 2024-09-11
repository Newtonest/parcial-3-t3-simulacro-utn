from servicio import * 


def mostrar_menu():
    print('0 - Salir ')
    print('1 - Cargar el arreglo pedido con los datos de n servicios')
    print('2 - Mostrar datos de servicios cuyo importe se encuentre en un intervalo especifico')
    print('3 - Mostrar cuantos servicios hay para cada tipo posible ')
    print('4 - Verificar si el cliente de algun servicio es igual a nom')
    opcion = validar_entre(0,4,'Elegir una opcion del menu de opciones: ')
    return opcion

def main():
    v = []
    op = -1
    while op != 0:
        op = mostrar_menu()
        if op == 1:
            n = validar_mayor_que(0,'Ingrese la cantidad de servicios que desea almacenar: ')
            v = cargar_arreglo(n)
        elif op == 0:
            print('Hasta prontooo')
        elif len(v) == 0:
            print('Tenes que cargar el vector primero')
        elif op == 2:
            inf = validar_mayor_que(0,'Ingrese el primer numero del intervalo: ')
            sup = validar_mayor_que(inf,'Ingrese el segundo numero del intervalo: ')
            ordenar_vector(v)
            mostrar_intervalo(inf,sup,v)
        elif op == 3:
            vector_de_conteo = contar(v)
            mostrar_vector(vector_de_conteo)
        elif op == 4:
            nom = input('Ingrese el nombre del cliente a buscar: ')
            buscar_cliente(nom,v)
if __name__ == '__main__':
    main()