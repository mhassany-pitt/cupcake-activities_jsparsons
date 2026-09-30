try:
    miarchivo=open(nombre_archivo, "r")
    num_linea=1
    for linea in miarchivo:
        palabras = linea.split()
        palabra=palabras[2]
        print("La tercera palabra en la linea",num_linea,"es",palabra)
        num_linea+=1
except OSError:
    print("Error al leer el archivo.")
