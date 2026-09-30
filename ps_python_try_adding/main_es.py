def sumar_dos_numeros(a,b):
    try:
        return a + b
    except TypeError:
        print("Solo se pueden sumar numeros.")
