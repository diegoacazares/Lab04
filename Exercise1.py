# Ejercicio 1: Escribe un programa que lea repetidamente números hasta
# que el usuario introduzca “fin”. Una vez se haya introducido “fin”,
# muestra por pantalla el total, la cantidad de números y la media de
# esos números. Si el usuario introduce cualquier otra cosa que no sea un
# número, detecta su fallo usando try y except, muestra un mensaje de
# error y pasa al número siguiente

total=0
counter=0
while True:
    try:
        input_str = input("Ingrese un número: ")
        if (input_str == "fin"):
            break
        else:
            total = total + int(input_str)
            counter = counter + 1
            average = total / counter
    except:
            print("valor no válido")
            continue
print("Total: ", + total)
print("Contador: ", + counter)
print("Promedio: ", + average)