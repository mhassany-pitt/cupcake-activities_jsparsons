cadena = "Madam"
n_cadena = cadena.lower()
cadena_invertida = ""
for caracter in n_cadena:
        cadena_invertida = caracter + cadena_invertida
if n_cadena == cadena_invertida:
        print("Esta cadena es un palindromo!")
else:
        print("La cadena no es un palindromo!")
