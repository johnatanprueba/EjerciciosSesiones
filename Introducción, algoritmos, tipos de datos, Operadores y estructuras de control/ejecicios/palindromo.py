palabra = "reconocer"
longitud = len(palabra)
j = longitud - 1
flagPalindromo = True

for i in range(0,longitud//2):
    if(palabra[i]!=palabra[j]):
        flagPalindromo = False
        break
    j=j-1

outTxt = "Es palindromo" if flagPalindromo else "No es palindromo"
print(outTxt)



