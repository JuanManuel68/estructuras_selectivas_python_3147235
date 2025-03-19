'''if else
determina dos caminos de ejecucion, basados 
en la evaulacion de una condicional
sintaxis:
if condicion:
    contruccion 1
    contruccion 2
else:
    contruccion 3
    contruccion 4
'''
#ejemplo
#elanore un programa en python que determine si una persona es mayor o menor de edad
#por lo tanto, habilitada para votar
edad = int(input("ingrese su edad: "))
doc = input("tiene documento? (SI/NO)")
if edad >= 18 and doc == "SI":
    print("Eres mayor de edad")
    print("puedes votar")
else:
    print("usted es menor de edad")
    print("o")
    print("no puede votar")
print("fin del programa")