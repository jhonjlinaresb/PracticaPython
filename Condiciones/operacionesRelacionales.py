'''Operaciones Relacionales
 Igualdad: ==
 Diferencia: !=
 Mayor que: >
 Menor que: <
 Mayor o igual que: >=
 Menor o igual que: <= '''

 #Ejemplo 1
edad = int(18) #Variable edad de tipo entero, con valor 18
if (edad == 18): #Si la edad es igual a 18, entonces:
    print("Su edad exactamente igual a 18") #Imprime: "Eres mayor de edad"
    if(edad > 18): #Si la edad es mayor a 18, entonces:
        print("Su edad es mayor a 18")
    else: #Si la edad es menor a 18, entonces:
            print("Su edad es menor a 18")
else: #Si la edad es no es mayor igual a 18, entonces:
    print("Su edad no es exactamente igual a 18")

#Ejemplo 2
edadDos = int(17)
if (edadDos != 18): #Si edad es distinto a 18, entonces:
    print("Su edad es diferente a 18") 
else: #Si la edad es igual a 18, entonces:
    print("Su edad no es distinta a 18") 

''' Ejemplo de uso:
----inicio----
Variable de edad: 18
Su edad exactamente igual a 18
Su edad es mayor a 18

Su edad es diferente a 18
fin --------'''