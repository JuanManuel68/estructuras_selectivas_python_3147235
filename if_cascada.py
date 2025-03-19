'''
if cascada:
estructura selectiva compuesta de multiples condicionales,
seguidos unos de otros
sintaxis:
if condicion1:
    instruccion1
    instruccion2
elif condicion2:
    instruccion3
    instruccion4
elif condicion3:
    instruccion5
    instruccion6
    
NOTA: cada condicional es mutuamente excluyente
'''
#ejemplo 
#hacer un pequeño traductor 
#el programa debe permitir leer por teclado una fruta en español
#y debe motrar esa fruta en ingles
fruta_es= input("ingrese una fruta: ")

if fruta_es == "manzana":
    print("apple")
elif fruta_es == "naranja":
    print("orange")
elif fruta_es =="uva":
    print("grape")
elif fruta_es =="pera":
    print("pear")
elif fruta_es=="fruta del dragon":
    print("dragon fruit")
#caso por defecto
#defaul    
else:
    print("no se reconoce la fruta")
    
edad = int(input("ingrese su edad: "))
estracto = input("tiene documento? (SI/NO)")
    