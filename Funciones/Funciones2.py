from statistics import mean

nota1 = 40; nota2 = 50; nota3 = 60   # Tres notas para probar la funcion


# definimos la funcion y le asignamos tres notas por defecto
def calcular_promedio(notas = [0, 3, 6]):
		# hacemos uso de las funciones preconstruidas en python sum() y len()
    promedio = sum(notas) / len(notas)
    return promedio

print(calcular_promedio([nota1, nota2, nota3])) # imprime 50.0