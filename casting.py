def casting():
    """Lee precio, descuento y cantidad como texto y calcula el precio con descuento y el total."""
    precio=float(input("Precio: "))
    des=float(input("Descuento: "))
    cant=float(input("Canatidad: "))
    total=(precio-des)*(cant)

    print("Precio:",int(precio))
    print("Descuento:",des)
    print("Precio con descuento:",(precio-des))
    print("Total:",total)


