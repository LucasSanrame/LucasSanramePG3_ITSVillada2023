meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agostini", "septiempre sin fap", "octubre", "no nuts november", "diciembre"]
try:
    mes_especifico = int(input("Ingrese el numero del mes que desea printear (0:enero, 1:febrero, 2:marzo, 3:abril, 4:mayo, 5:junio, 6:julio, 7:agostini, 8:septiembrin, 9:octoberfest, 10:nnn, 11:diciembrin)"))
except IndexError:
    print("ese objeto no esta en la lista")
finally:
    print(meses[mes_especifico])