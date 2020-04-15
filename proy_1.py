sw =True
def menu():
    print('=====MENU====')
    print('\t1. Sumar')
    print('\t2. Restar')
    print('\t3. Multiplicar')
    print('\t4. Dividir')
    print('\t5. Salir')

def salir():
    print('Fin del programa')
    global sw
    sw = False
while sw:
    menu()
    print('¿Que desea realizar? ')
    opcionMenu = input('Inserte una opcion:')

    if opcionMenu == '1':
        a=int(input('Ingrese el primer valor: '))
        print('+')
        b = int(input('Ingrese el segundo valor: '))
        c=a+b
        print('La suma es: ',c)

        input('Has pulsado la opción 1...\npulsa una tecla para continuar')
    elif opcionMenu == '2':
        a = int(input('Ingrese el primer valor: '))
        print('-')
        b = int(input('Ingrese el segundo valor: '))
        c = a - b
        print('La resta es: ', c)

        input('Has pulsado la opción 2...\npulsa una tecla para continuar')
    elif opcionMenu == '3':
        a = int(input('Ingrese el primer valor: '))
        print('*')
        b = int(input('Ingrese el segundo valor: '))
        c = a * b
        print('La multiplicacion es: ', c)
        print('Has pulsado la opción 3...\npulsa una tecla para continuar')

    elif opcionMenu == '4':
        a = float(input('Ingrese el primer valor: '))
        print('/')
        b = float(input('Ingrese el segundo valor: '))
        c = a / b
        print('La division es: ', c)

        print('Has pulsado la opción 3...\npulsa una tecla para continuar')
    elif opcionMenu== '5':
        salir()
