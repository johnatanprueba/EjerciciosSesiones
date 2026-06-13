
file = None
try:
  file = open("archivo.txt","r")
except FileNotFoundError as e:
    print("Ocurrio un error aca:",e)
finally:
    if file:
       file.close()
