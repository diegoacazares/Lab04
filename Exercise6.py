# Ejercicio 6: Escribe el programa de cálculo del salario, con 
# tarifa-ymedia para las horas extras, y crea una función llamada
# calculo_salario que reciba dos parámetros (horas y tarifa).

def calcularSalario(horas, tarifa):
    horas_extras = horas - MAX_HORAS_SEMANALES
    if(horas_extras > 0):
        salario = (MAX_HORAS_SEMANALES * tarifa) + (horas_extras * (tarifa * 1.5))
    else: 
        salario = horas * tarifa
    return salario

try: 
    MAX_HORAS_SEMANALES = 40
    horas = int(input("Ingrese número de horas: "))
    tarifa = float(input("Ingrese la tarifa por hora: "))
    salario = calcularSalario (horas,tarifa)
    print(salario)
except:
        print("#Error, debe ingresar un valor númerico")
