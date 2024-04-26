try:
    with open("Ej5.txt", "w") as carpeta:
       carpeta.write("AMERICA YA!")
       for numero in range(1, 90):
          carpeta.write(" HALLO ")
except Exception as e:
    print(e)











