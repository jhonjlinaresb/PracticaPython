'''Crear un programa que genere tablas de multiplicar
ToDo: For Loop'''

numero = int(input("Ingrese un numero: "))
limite = int(input("Ingrese el limite: "))
texto = ""
def tabla(numero, limite):
    for numero in range(limite):
        print(texto * limite)
        numero = numero + 1
        print(numero * limite)

tabla(numero, limite)