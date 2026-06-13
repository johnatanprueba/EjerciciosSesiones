import csv
import json
with open("ejercicioDiapo.txt","w") as archivo:
    archivo.write("Hola Mundo") 
print("Texto guardado en txt...")

with open("ejercicioDiapo.csv","w",newline="") as archivo:
    escritor = csv.writer(archivo)
    escritor.writerow(["nombre","ciudad"])
    escritor.writerow(["Viviana","Barranca"])
    escritor.writerow(["Juan","Bucaramanga"])
print("Datos guardados en csv ")

with open("ejercicioDiapo.json","w") as archivo:
    datos = {
        "nombre":"Susana",
        "edad":"26",
        "materias":[{"nombremateria":"matematicas","calificacion":4.5}
                    ,{"nombremateria":"biologia","calificacion":3.5}]
    }
    json.dump(datos,archivo,indent=4)
print("Datos guardados en json ")

with open("ejercicioDiapo.txt","r+") as archivo:
    for row in archivo:
        print(row.strip())

print("Esto es el contenido del archivo csv")
with open("ejercicioDiapo.csv","r",newline="") as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)

print("Esto es el contenido del archivo JSON")
with open("ejercicioDiapo.json","r") as archivo:
    datosCargados = json.load(archivo)
    print("Contenido del json:",datosCargados)

