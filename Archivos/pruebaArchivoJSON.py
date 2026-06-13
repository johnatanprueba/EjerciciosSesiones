import json

with open("datos.json","r") as archivo:
    datos_cargados = json.load(archivo)
    print("Datos cargados:",datos_cargados)