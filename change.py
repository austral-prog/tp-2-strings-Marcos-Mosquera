def change():
    """Lee un gasto y el dinero recibido, calcula el vuelto
    y lo separa en pesos (parte entera) y centavos.

    """
    gasto=float(input("Gasto: "))
    ganancia=float(input("Ganancia: "))
    vuelto=ganancia-gasto
    vuelto_c=vuelto-int(vuelto)

    print("Pesos:",int(vuelto))
    print("Centavos:",int(vuelto_c*100))

    pass

change()