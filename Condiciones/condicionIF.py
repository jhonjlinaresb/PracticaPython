'''Crear un programa que lea una variable y cumpla la condicion: 
Si el numero es Mayor 17, imprima: "Eres mayor de edad"
Si el numero es Menor o igual a 17, imprima: "Eres menor de edad"'''

edad = int(input("Ingrese su edad: ")) #edad es una variable de tipo entero, pide una edad al usuario con INPUT

if (edad > 17): #Si la edad es mayor a 17, entonces:
    print("Eres mayor de edad") #Imprime: "Eres mayor de edad"
else: #Si la edad es no es mayor a 17, entonces:
    print("Eres menor de edad") #Imprime: "Eres menor de edad"

''' Ejemplo de uso:
Ingrese su edad: 18
Eres mayor de edad '''
