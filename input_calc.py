def rectangle():
    """Lee base y altura de un rectángulo, calcula e imprime
    el área y el perímetro.
    """
    base=int(input("Base: "))
    altura=int(input("Altura: "))
    print("Area:", base*altura)
    print("Perimetro:", (base*2)+(altura*2))


    pass

rectangle()