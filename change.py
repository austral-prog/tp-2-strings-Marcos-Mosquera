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
    
    print("Pesos:")
    print(int(vuelto))
    print("Centavos:")
    print(round(vuelto_c*100))

