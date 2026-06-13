def frecuencia_letras(cadena):
    cadenaResultado = {}
    for e in cadena:
        if e!=" " and e!="!" and e!="." and e!="," and e!="?":
            ele = e.lower()
            if ele in cadenaResultado.keys():
                cadenaResultado[ele]=cadenaResultado[ele]+1
            else:
                cadenaResultado[ele]=1
    return cadenaResultado

cadena = "Hola , mundo! Python es genial." 
resultado = frecuencia_letras(cadena)

print(resultado)