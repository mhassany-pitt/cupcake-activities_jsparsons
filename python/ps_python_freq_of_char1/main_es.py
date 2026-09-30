def frecuencia_de_caracter(cadena):
        num_de_caracter = {}
        for letra in cadena:
                if letra in num_de_caracter:
                        num_de_caracter[letra] += 1
                else:
                        num_de_caracter[letra] = 1
        return num_de_caracter
