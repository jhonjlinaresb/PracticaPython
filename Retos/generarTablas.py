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

''' Ejemplo de uso:
-----Inicio-----
Ingrese un numero: 5
Ingrese el limite: 10
5 x 0 = 0
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
5 x 4 = 20
5 x 5 = 25
5 x 6 = 30
5 x 7 = 35
5 x 8 = 40
5 x 9 = 45
-----Fin--------'''