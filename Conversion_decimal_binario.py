opciones = ["1. Decimal a binario", 
            "2. Binario a decimal"]

while True:
    print("--- CONVERSION --- ")
    print(" --- MENU --- ")
    for opcion in opciones:
        print(opcion)

    seleccion = input("Seleccione una opcion: ")

    if (seleccion == "1"):
        decimal = int(input("Ingrese el numero decimal que desea convertir: "))
        binario = ""

        while decimal > 0:
            binario = str(decimal % 2) + binario
            decimal = decimal // 2
        print(f"Su conversion a binario es = {binario}")
        

    elif (seleccion == "2"):
        bin = input("Ingrese el numero binario que desea convertir: ")
        dec = int(bin, 2)
        print(f"Su conversion a decimal es: {dec}")
    break
