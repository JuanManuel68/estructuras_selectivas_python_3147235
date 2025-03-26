'''
actividad 3
elaborar un programa que permita calculas el salario neto de un empleo ,
despues de descontar los descuentos por conceptos de:
salud, pension, Arl
1.el programa debe solicitar el tipo de empleado:
    a.contrato a termino indefinido
        (el contrato de prestacion de servicios debe solicitar
        -antiguedad en años
        -grado o escalafon(1-5)
        -el salario minimo
        el salario mensual, se calcula deacuerdo a la siguiente tabla:
        -grado 1: 1.5 sm
        -grado 2: 1.7 sm
        -grado 3: 2.0 sm
        -grado 4: 2.5 sm
        -grado 5: 3.0 sm
        la bonificacion estara acorde a los siguientes rangos segun la antiguedad
        -entre 1 y 5 años: 1% del salario mensual
        -entre 6 y 10 años: 2% del salario mensual
        -superior a 10 : 3% del salario mensual
        para este caso, los descuentos de ley son:
        -25% por concepto a eps
        -20% por concepto a pensión
        -15% por concepto a arl
        )
    b.contrato por prestacion de servicio
        (el contrato de prestacion de servicios debe solicitar
        -el valor del contrato
        -numero de meses del contrato 
        -la antiguedad del empleado(años)
        el salario neto, se calcula :
        1-dividir el valor de contrato por el numero de meses(salario mensual)
        2-restar el 15% del valor anterior por concepto de EPS(salud)
        3- restar el 10% de valor del salario mensual, por concepto de pension
        4-si el empleado tiene una antiguedad igual o superior de 10años:
        tendra una bonificacion del 0.5% sobre el salario mensual)
        
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
    print("Eligió: contrato a término indefinido")
    anti = int(input("Ingrese la antigüedad del empleado (años): "))
    grado = int(input("Ingrese el grado o escalafón del empleado (1-5): "))
    salario_min = int(input("Ingrese el valor del salario mínimo: "))
    
    if grado == 1:
        salario_men = salario_min * 1.5
    elif grado == 2:
        salario_men = salario_min * 1.7
    elif grado == 3:
        salario_men = salario_min * 2.0
    elif grado == 4:
        salario_men = salario_min * 2.5
    elif grado == 5:
        salario_men = salario_min * 3.0
    else:
        print("Grado no válido")
        salario_men = 0
    if anti <= 5:
        bono = salario_men * 0.01  
    elif anti <= 10:
        bono = salario_men * 0.02 
    else:
        bono = salario_men * 0.03 
    eps = salario_men * 0.25 
    pension = salario_men * 0.20  
    arl = salario_men * 0.15  
    salario_neto = salario_men + bono - eps - pension - arl    
elif contrato == "b":
    print("eligio: contrato por prestacion de servicio")
    valor_contrato = int(input("ingrese el valor del contrato: "))
    num_meses = int(input("ingrese el numero de meses del contrato: "))
    antiguedad = int(input("ingrese la antiguedad del empleado (años): "))
    salario_mensual = valor_contrato / num_meses
    eps = salario_mensual * 0.15
    pension = salario_mensual * 0.10
    bonificacion = salario_mensual * 0.5
    salario_neto = salario_mensual - eps - pension
    if antiguedad >= 10:
        salario_neto = salario_mensual + bonificacion
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