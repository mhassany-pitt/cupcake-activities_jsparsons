indice_min = 0
indice_max = 0
for indice in range(1, len(num_lista)):
    if num_lista[indice] < num_lista[indice_min]:
        indice_min = indice
    if num_lista[indice] > num_lista[indice_max]:
        indice_max = indice
print(indice_min, indice_max)
