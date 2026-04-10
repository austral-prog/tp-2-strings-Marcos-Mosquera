def string_methods():
    """Demuestra el uso de métodos de string: strip, lstrip, rstrip, upper, lower,
    title, find, replace, count, operador in, slicing con paso, reverso,
    f-strings y strings multilínea.
    """
    nombre = "   Grace Hopper   "
    frase = "Python es un gran lenguaje de programacion"
    multilinea = """Linea 1
Linea 2
Linea 3"""

    print(F"Strip: {nombre.strip()}")
    print(F"Lstrip: {nombre.lstrip()}")
    print(F"Rstrip: {nombre.rstrip()}")
    print(F"Upper: {frase.upper()}")
    print(F"Lower: {frase.lower()}")
    print(F"Title: {frase.title()}")
    print(F"Find: {frase.find('g')}")
    print(F"Replace: {frase.replace('programacion','desarrollo')}")
    print(F"Count: {frase.count('a')}")
    print(F"Contiene Python: {'Python' in frase}")
    print(F"Contiene Java: {'Java' in frase}")
    print(F"Slice: {frase[:6:]}")
    print(F"Paso: {frase[:6:2]}")
    print(F"Reverso: {frase[5::-1]}")
    print(F"Formato: {nombre.strip()} sabe {frase[:6:]}")
    print(F"{multilinea}")



