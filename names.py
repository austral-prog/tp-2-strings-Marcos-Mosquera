def names():
    """Lee nombre y apellido, e imprime el nombre completo en distintos formatos:
    minúsculas, título, mayúsculas y con tabulador.
    """
    primer=input("Primer nombre: ")
    apellido=input("Apellido: ")
    nombre=primer+" "+apellido
    print(nombre.lower())
    print(nombre.title())
    print(nombre.upper())
    print(f"\t{nombre.lower()}")
