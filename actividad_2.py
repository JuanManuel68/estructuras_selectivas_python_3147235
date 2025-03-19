edad = int(input("Ingrese su edad: "))
extracto = input("Ingrese su extracto (1 o 2): ")
pre = int(input("Ingrese el valor de la matrícula: "))


if edad < 18 and extracto == "1":
    des = pre * 0.20
    print("Usted tendrá un descuento del 20% del total de la matrícula: ",des)
elif edad >= 18 and extracto == "1":
    des = pre * 0.15
    print("Usted tendrá un descuento del 15% del total de la matrícula: ",des)
elif edad < 18 and extracto == "2":
    des = pre * 0.10
    print("Usted tendrá un descuento del 10% del total de la matrícula: ",des)
elif edad >= 18 and extracto == "2":
    des = pre * 0.05
    print("Usted tendrá un descuento del 5% del total de la matrícula: ",des)
else:
    print("Datos inválidos. Asegúrese de ingresar valores correctos para la edad y el extracto.")
    
totalpagar = pre - des
print ("su total a pagar de la matricula es ",totalpagar)