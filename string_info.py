def string_info():
    """Dada la palabra 'Programacion', imprime su longitud, primera y última letra,
    la palabra repetida 3 veces y decorada con '***'.
    """
    palabra = "Programacion"
    print(f"""
Palabra: {palabra}
longitud: {len(palabra)}          
Primera letra: {palabra[0]}
Ultima letra: {palabra[-1]}
Repetida: {palabra*3}
Decorada: ***{palabra}***         
          """)
    
string_info()