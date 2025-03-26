'''
if anidados
if dentro de otros if:
sintaxis
if condicion1:
    if condicion2:
        print("mensaje")
        if condicion2:
            print("mensaje2")
            if condicion3:
                print("mensaje3")
                if condicion4:
                    print("mensaje4")
    else:
        print("mensaje")
"no confundir con elif(if en cascada)
'''
#ejemplo 1:
#modifique el ejercicio de la edad para que las siguientes condiciones:
#1.si es mayor a 18 años pero no tiene documento, no puede votar
#2.si es menor de 18 años no puede votar
#utilize estructura de if anidados 

edad = int(input("ingrese su edad: "))
if edad>=18 :
    documento = input("tiene documento? si/no: ")
    if documento == "si" :
        print("puede votar")
    else:
        print("no puede votar, no tiene documento")
else:
    print("no puede votar, es menor de edad")