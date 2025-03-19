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
edad = 18
doc = False
if edad >= 18 and doc == True:
    print("Eres mayor de edad")
    print("puedes votar")
else:
    print("usted es menor de edad")
    print("o")
    print("no puede votar")
print("fin del programa")