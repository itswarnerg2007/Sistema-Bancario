saldo=int(input("Ingrese su saldo: "))
opcion=0

while opcion!=4:
    print("======Cajero Automatico======")
    print("1. Consultar Saldo")
    print ("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Salir")

    opcion= int(input("Ingrese una opcion: "))

    if opcion==1:
        print("Su saldo es: ", saldo)

    elif opcion==2:
        cantidad= float(input("Ingrese la cantidad a depositar: "))
        saldo+=cantidad
        print("Deposito exitoso. Su nuevo saldo es: ", saldo)

    elif opcion==3:
        cantidad= float(input("Ingrese la cantidad a retirar: "))
        if cantidad<=saldo:
            saldo-=cantidad
            print("Retiro exitoso. Su nuevo saldo es: ", saldo)
        else:
            print("Fondos insuficientes.")
    elif opcion==4:
        print("Gracias por usar el cajero automatico.")
    else:
        print("Opcion invalida. Por favor, ingrese una opcion valida.")
