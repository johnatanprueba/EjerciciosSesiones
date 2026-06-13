import csv

with open("ejemploCsv.csv","r",newline="") as archivo:
    dicVal =  csv.DictReader(archivo)
    for fila in dicVal:
        print(f"{fila["nombre"]}, tiene una edad de {fila["edad"]} y vive en {fila["ciudad"]}")

    