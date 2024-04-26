ads ="si"
while ads == "si":
    try:
        x1 = int(input("Ingrese un numero a sumar: "))
        x2 = int(input("Ingrese otro numero a sumar: "))
    except:
        print("solo se aceptan datos numericos")
    finally:
        resultado = x1 + x2
        print(resultado)
        ads = input("Quieres hacerlo otra vez? ")