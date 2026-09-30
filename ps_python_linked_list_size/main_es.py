def obtener_tamano(lista_enlazada):
    contador = 0
    temp = lista_enlazada.cabeza
    while temp:
        contador = contador + 1
        temp = temp.siguiente
    return contador
