def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.

    """
    print("Ingresar gasto:")
    gasto=float(input())
    print(gasto)
    print("Dinero recibido")
    ganancia=int(input())
    print(ganancia)

    print("")
    print("Vuelto")
    print("")

    vuelto=float(ganancia-gasto)
    vuelto_c=vuelto-int(vuelto)
    vuelto_p=vuelto-vuelto_c
    print(vuelto)

    print("Pesos:")
    print(int(vuelto_p))
    print("Centavos:")
    print(int(vuelto_c*100))

