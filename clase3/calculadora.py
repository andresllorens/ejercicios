def calculadora(arg1: int, arg2: int, operador: str):
    if (operador == '+'):
        r = arg1 + arg2
        return r
    
    elif (operador == '-'):
        r = arg1 - arg2
        return r

    elif (operador == '*'):
        r = arg1 * arg2
        return r

    elif (operador == '/'):
        r = arg1 / arg2
        return r

    else:
        return 'Operacion Invalida'



print('Bienvenido \n')
a = int(input("Ingrese un numero: "))
b = int(input("Ingrese otro numero: "))
c = input("Ingrese el operador +, -, * o / : ")

rta = calculadora(a, b, c)
print("\nrta= ", rta)
input("\nEnter para Salir")
