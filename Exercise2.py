# Ejercicio 2: Escribe otro programa que pida una lista de números como
# la anterior y al final muestre por pantalla el máximo y mínimo de los
# números, en vez de la media.

minimo = 0
maximo = 0
primerNumero = True
while True:
    numero = input ("Ingrese un número: ")
    if(numero == "salir"):
        break

    if (primerNumero):
        minimo = int(numero)
        maximo= minimo
        primerNumero= False
    else:
        if (int(numero)>maximo):
            maximo = int(numero)
        if(int(numero)<minimo):
            minimo = int(numero)
print ("Máximo", maximo)
print ("Mínimo", minimo)