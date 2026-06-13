def duplicarDeeper(listaTuplas):
    listaCopia = []
    for fila in listaTuplas:
        listaCopia.append(fila)
    return listaCopia

def intercambiarLibros(listaTuplas):
    listaInter = []
    for tupla in listaTuplas:
       listaInter.append((tupla[0],tupla[2],tupla[1]))
    return listaInter

librosDisponibles = [('El Perfume', 'Suskind', 'Misterio'),
                    ('La Metamorfosis', 'Kafka', 'Novela'), 
                    ('Misery', 'Stephen King', 'Misterio'), 
                    ('Harry Potter', 'J.K. Rowling', 'Novela'), 
                    ('El Principito', 'Saint-Exupery', 'Infantil'), 
                    ('El Codigo Da Vinci', 'Dan Brown', 'Misterio')]

librosDisponiblesCopia = duplicarDeeper(librosDisponibles)

librosDisponibles.sort(key=lambda t:len(t[0]))

print(librosDisponibles)
print("==============================")
print(librosDisponiblesCopia)
print("==============================")
listaLibrosInterCam = intercambiarLibros(librosDisponiblesCopia)
print(listaLibrosInterCam)


