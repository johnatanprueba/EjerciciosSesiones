repisa = ['Peluche', 'Libro', 'celular', 'lampara']
objetos = iter(repisa)


print(next(objetos)) # Imprime Peluche
print(next(objetos)) # Imprime Libro
print(next(objetos)) # Imprime celular
print(next(objetos)) # Imprime lampara


print(next(objetos)) # Error StopIteration