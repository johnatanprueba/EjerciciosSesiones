from collections.abc import Iterable

def es_iterable(obj):
    print(issubclass(type(obj), Iterable))

nivel = 3
cadena  = "cadena"
tupla = ('tupla1', 'tupla2'), 
lista =  ['l', 'i', 's', 't', 'a', 's']                                                         
diccionario = { 'diccionario1' : {} , 'diccionario2' : {}} 
cadena = ""

es_iterable(nivel)        # False
es_iterable(cadena)       # True
es_iterable(tupla)        # True
es_iterable(lista)        # True
es_iterable(diccionario)  # True
es_iterable(cadena)       # True