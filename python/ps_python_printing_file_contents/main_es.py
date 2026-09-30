try:
archivo_a_leer = open(nombre_archivo, "r")
fila = archivo_a_leer.readline()
while fila != "":
print(fila)
fila = archivo_a_leer.readline()
archivo_a_leer.close()
except OSError:
print("Error al leer el archivo. La ejecucion del programa termina.")
