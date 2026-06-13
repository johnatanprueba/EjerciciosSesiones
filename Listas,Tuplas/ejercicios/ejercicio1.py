#Ejercicio 1
lista = ["laptop", "mouse", "laptop", "teclado", "mouse", "monitor", "laptop"]
listaElementosUnicos = []
for elem in lista:
    if not elem in listaElementosUnicos:
        listaElementosUnicos.append(elem)

print(listaElementosUnicos) #1 

listaTuplas = []
for elem in listaElementosUnicos:
    tpl = (elem,lista.count(elem))
    listaTuplas.append(tpl)

print(listaTuplas) #2

listaTuplas.sort(key=lambda x:x[0])

for elem in listaTuplas:
    print(str(elem[0])+":"+str(elem[1])+" unidades vendidas") #3

listaTuplas.sort(key=lambda x:x[1],reverse=True)
tplMasVe = listaTuplas[0]
print(tplMasVe[0]) #4
