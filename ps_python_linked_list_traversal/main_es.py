def recorrer_lista(lista_doble):
    actual = lista_doble.cabeza
    while actual:
        print(actual.dato, end=" ")
        ultimo = actual
        actual = actual.siguiente
    while ultimo:
        print(ultimo.dato, end=" ")
        ultimo = ultimo.anterior
