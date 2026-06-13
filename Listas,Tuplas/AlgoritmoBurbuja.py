lista = [10,3,5,6,4,1,2,9]

for i in range(0,len(lista)-1):
    for j in range(i+1,len(lista)):
        if lista[j]<lista[i]:
            temp = lista[i]
            lista[i] = lista[j]
            lista[j] = temp

print(lista)