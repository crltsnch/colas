#Básicamente el concepto de colas es que el Primer elemento ingresado es el primero en salir. Un ejemplo clásico es el de una fila de un banco.

#Creamos una lista vacía
cola = []

#Creamos un menú con 4 opciones
def main():
    print('1 Insertar')
    print('2 Borrar')
    print('3 Listar')
    print('4 Salir')
    option = int(input('Elija una opción: '))

    #Esto encola el número en la lista
    if option == 1:
        elemento = input('Introduzca el numero a encolar: ')
        