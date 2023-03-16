# Calculadora em Python

print("\n******************* Python Calculator *******************")


def Suma(a,b):
    return a + b

def Resta(a,b):
    return a - b

def Multi(a,b):
    return a * b

def Divi(a,b):
    return a / b


print("\nSeleccione el número de operación deseada: \n")
print("1 - Suma")
print("2 - Resta")
print("3 - Multiplicación")
print("4 - División")

selec = input("\nDigite una opcion (1/2/3/4): ")


while True:
    try:
        num1 = int(input("\nDigite el primer número: "))
        break
    except ValueError:
        print("Valor inválido")

while True:
    try:
        num2 = int(input("\nDigite el segundo número: "))
        break
    except ValueError:
        print("Valor inválido")


if selec == "1":
    print(num1, "+", num2, "=", Suma(num1, num2))
    
elif selec == "2":
    print(num1, "-", num2, "=", Resta(num1, num2))
    
elif selec == "3":
    print(num1, "*", num2, "=", Multi(num1, num2))
    
elif selec == "4":
    try:
        print(num1, "/", num2, "=", Divi(num1, num2))
    except ZeroDivisionError:
        print("No se puede dividir por cero")

else:
    print("\nOpción Inválida!")