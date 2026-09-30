def ordenamiento_rapido(datos, primero, ultimo):
    if primero < ultimo:
        pivote = particion(datos, primero, ultimo)
        ordenamiento_rapido(datos, primero, pivote-1)
        ordenamiento_rapido(datos, pivote+1, ultimo)
    return datos
