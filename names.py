def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """
    nombre=input("nombre: ")
    print(nombre.lower())
    print(nombre.title())
    print(nombre.upper())
    print(f" \t {nombre}")
    pass

names()