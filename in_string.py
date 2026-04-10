def check_vowels():
    """Lee un nombre y verifica si contiene cada una de las vocales (a, e, i, o, u),
    sin distinguir mayúsculas de minúsculas.
    """

    nombre=(input("Nombre: "))
    print("Contiene a:", ("a" in nombre.lower()))
    print("Contiene e:", ("e" in nombre.lower()))
    print("Contiene i:", ("i" in nombre.lower()))
    print("Contiene o:", ("o" in nombre.lower()))
    print("Contiene u:", ("u" in nombre.lower()))    
