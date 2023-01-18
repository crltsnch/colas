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
        cola.append(elemento)
        print('Número encolado con éxito')
        main()
    
    #Esta opción saca de la lista el numero en orden de ingreso
    elif option == 2:
        if len(cola)>0:
            print('El numero: ', cola.pop(0), 'fue desencolado')
            main()
        else:
            print('Cola vacía')
            main() 

    #Esta opción imprime en pantalla la cola
    elif option == 3:
        for i in cola:
            print('Cola: ', i)       
        main()
    
    #Esta opción permite salir de la ejecución del código
    elif option == 4:
        exit()
    else:
        print('Seleccione una opción valida: ')
        main()

print(main())