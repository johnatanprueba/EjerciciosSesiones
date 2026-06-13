import json


file =  open("archivoJSON.json") 
users = json.load(file)


for user in users:
    print("Nombre del usuario:", user["name"], ", edad:", user["age"])
file.close()