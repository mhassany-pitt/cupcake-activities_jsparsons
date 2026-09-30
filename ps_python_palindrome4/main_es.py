def es_palindromo(cadena):
        i = 0
        j = len(cadena) - 1
        n_cadena = cadena.lower()
        while i < j:
                if n_cadena[i] != n_cadena[j]:
                        return False
                i += 1
                j -= 1
        return True
