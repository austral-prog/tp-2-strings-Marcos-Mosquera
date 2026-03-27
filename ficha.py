def ficha():
    """Ejercicio integrador. Lee nombre, email y 3 notas, y genera una ficha
    de alumno aplicando: strip, title, lower, upper, int, len, find, slicing,
    reverse, replace, count, in, f-strings, strings multilínea y operaciones matemáticas.
    """
    # Ejercicio integrador: Generador de Ficha de Alumno
    #
    # Leer mediante input:
    #   1. Nombre completo (puede tener espacios extra y mayúsculas mezcladas)
    #   2. Email (puede tener mayúsculas)
    #   3. Tres notas (como texto, hay que convertirlas)
    #
    # Generar una ficha que incluya:
    #   - Encabezado decorativo usando un string multilínea con "="
    #   - Nombre limpio: sin espacios extra y con formato título
    #   - Email en minúsculas
    #   - Cantidad de caracteres del nombre
    #   - Iniciales: usar find para encontrar el espacio e indexar las letras
    #   - Usuario: apellido.nombre en minúsculas
    #   - Verificar si el email contiene @ 
    #   - Extraer el dominio del email
    #   - Nombre con guion bajo en vez de espacio
    #   - Contar las 'a' en el nombre
    #   - Código secreto: nombre invertido en mayúsculas
    #   - Las 3 notas, su suma, promedio y promedio entero
    #   - Cierre decorativo usando repetición de string ("=" * 24)
    nombre=input("Nombre: ").strip().title()
    mail=input("mail: ").lower()
    n1=int(input("Valor de la primera nota: "))
    n2=int(input("Valor de la segunda nota: "))
    n3=int(input("Valor de la tercera nota: "))
    iniciales=nombre[0]+nombre[nombre.find(" ")+1]
    usuario=nombre.replace(" ",".")
    archivo=nombre[nombre.find(" ")+1:]+"_"+nombre[:nombre.find(" ")]
    



    print(f"""
========================
    Ficha del Alumno          
========================
Nombre: {nombre}
Email: {mail}
Caracteres en nombre: {len(nombre)}
Iniciales: {iniciales.upper()}
Usuario: {usuario.lower()}
Email valido: {("@" in mail)}
Dominio: {mail[mail.find("@")+1:]}
Nombre de archivo: {archivo.lower()}
Cantidad de a: {nombre.count("a")}
Codigo secreto: {nombre.upper()[::-1]}
Nota 1: {n1}
Nota 2: {n2}
Nota 3: {n3}
Suma: {n1+n2+n3}
Promedio: {(n1+n2+n3)/3}
Promedio entero: {int((n1+n2+n3)/3)}
""")




    pass

ficha()