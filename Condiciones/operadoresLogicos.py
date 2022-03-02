'''Practicaremos los operadores logicos en este ejercicio
and, or, not, is, is not, in, not in
y, o, no, es, no es, en, no en'''

#Ejercicio 1:
edad = int(20)

if (edad >= 18 and edad < 30): #Debe cumplir con ambas condiciones
    print("Su edad es mayor a 18 y menor a 30")
else:
    print("Su edad no es mayor a 18 y menor a 30")

#Ejercicio 2:

pago = int(25)
valorEntrada = int(25)
if (pago >= valorEntrada or pago == valorEntrada): #Debe cumplir con alguna de las condiciones
    print("Puede pasar al teatro")
    if (pago != valorEntrada): #Si es diferente al valor de la entrada
        cantidadDevuelta = int(pago - valorEntrada)
        print("Le devolvemos €" + str(cantidadDevuelta)) #Convierte el valor de cantidadDevuelta a string
    else:
        print("No le devolvemos nada") #Si el pago es igual al valor de la entrada
else:
    print("No puede pasar al teatro porque no ha pagado la cantidad de entrada")

#Ejercicio 3 - Negacion ejemplo:

ofertas = int(9)

if (not ofertas > 10):
    print ("Hay varias ofertas")
else:
    print ("NO")