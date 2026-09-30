def es_palindromo(cadena):
        n_cadena = cadena.lower()
        cadena_invertida = ""
        for caracter in n_cadena:
                cadena_invertida = caracter + cadena_invertida
        if n_cadena == cadena_invertida:
                return True
        else:
                return False
