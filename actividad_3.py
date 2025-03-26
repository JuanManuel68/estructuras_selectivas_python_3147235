'''
actividad 3
elaborar un programa que permita calculas el salario neto de un empleo ,
despues de descontar los descuentos por conceptos de:
salud, pension, Arl
1.el programa debe solicitar el tipo de empleado:
    a.contrato a termino indefinido
    b.contrato por prestacion de servicio
    c.contrato de aprendizaje
        ()
    d.contrato por jornal(freelance)
        (el fornal debe solicitar
        -numero de horas trabajadas
        -el valor a pagar
        *el total del salario se calcula de multiplicar el 
        de horas por el valor a pagar por hora)
'''
contrato = input("ingrese el tipo de contrato: ")
salario_neto=0

if contrato == "a":
    print("eligio: contrato a termino indefinido")
elif contrato == "b":
    print("eligio: contrato por prestacion de servicio")
elif contrato == "c":
    print("eligio: contrato de aprendizaje")
    salario_minimo= int(input("ingrese el valor del salario minimo"))
    salario_neto = salario_minimo - salario_minimo * 0.25
elif contrato == "d":
    print("eligio: contrato por jornal(freelance)")
    numero_horas=int(input("ingrese numero de horas: "))
    valor_hora=int (input("ingrese el valos por hora a pagar: "))
    salario_neto=numero_horas*valor_hora
else:
    print("tipo de contrato no existe")
print("el salario neto es: ",salario_neto)
print("fin del programa")