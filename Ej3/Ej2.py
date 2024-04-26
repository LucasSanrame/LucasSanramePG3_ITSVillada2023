try:
    x1 = int(input("Ingrese un numero a dividir: "))
    x2 = int(input("Ingrese otro numero a dividir: "))
    division = x1 / x2
    print(division)
except ZeroDivisionError:
    print("no se puede dividir por 0")