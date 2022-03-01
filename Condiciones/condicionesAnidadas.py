'''Crear un programa que realice doble verificación
Se usará if anidado'''

edad = int(input("Ingrese su edad: ")) #edad es una variable de tipo entero, pide una edad al usuario con INPUT
pago = bool(False) #pago es una variable de tipo booleano

if (edad >= 18): #Si la edad es mayor o igual a 18,
    if (pago == True): #Si el pago es verdadero, entonces:
        print("Es mayor de edad y puede pasar porque el pago es verdadero") #Imprime: "Es mayor de edad y puede pasar"
    else: #Si el pago es falso, entonces:
        print("Es mayor de edad y no puede pasar porque el pago es falso") #Imprime: "Es mayor de edad y no puede pasar"
else: #Si la edad es menor a 18, entonces:
    print("Es menor de edad") #Imprime: "Es menor de edad"

''' Ejemplo de uso:
-----Inicio-----
Ingrese su edad: 18
Pago verdadero
Es mayor de edad y puede pasar
Pago falso
Es mayor de edad y no puede pasar
Ingrese su edad: 17
Es menor de edad 
Fin --------'''