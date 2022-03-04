'''Crear un programa que genere tablas de multiplicar
ToDo: For Loop'''

numero = int(input("Ingrese un numero: "))
limite = int(input("Ingrese el limite: "))
#-Crear un for loop que imprima la tabla de multiplicar del numero y limite ingresado
def tabla(numero, limite):
    for f in range(0, limite):
        generar = numero * f #Genera la tabla de multiplicar
        print(f'{numero} x {f} = {generar}') #Imprime la tabla de multiplicar

tabla(numero, limite)