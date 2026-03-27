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

    print(F"""
Strip: {nombre.strip()}
Lstrip: {nombre.lstrip()}
Rstrip: {nombre.rstrip()}
Upper: {frase.upper()}
Lower: {frase.lower()}
Title: {frase.title()}
Find: {frase.find("gran")}
Replace: {frase.replace("programacion","desarrollo")}
Count: {frase.count("a")}
Contiene Python: {"Python" in frase}
Contiene Java: {"Java" in frase}
Slice: {frase[:6:]}
Paso: {frase[:6:2]}
Reverso: {frase[6:0:-1]}
Formato: {nombre.strip()} sabe {frase[:6:]}
{multilinea}

""")



string_methods()