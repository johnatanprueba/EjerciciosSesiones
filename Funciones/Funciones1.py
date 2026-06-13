def calcular_promedio_de_3_notas(notaA = 0, notaB = 3, nota3 = 6):
	if(isinstance(nota3,str) or notaA<0 or notaB<0 or nota3<0 or notaA>100 or notaB>100 or nota3>100):
		print("No son valores validos")
		return
	promedio = (notaA + notaB + nota3) / 3
	return promedio

promedio = calcular_promedio_de_3_notas()
print(promedio)
calcular_promedio_de_3_notas(1000 ** 1000, 10+40, 500 / 5 )
print(calcular_promedio_de_3_notas(100, 100, "cien"))
