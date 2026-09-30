def mezcla(datos):
    if len(datos) <= 1:
        return datos
    mitad = len(datos)//2
    izquierda = mezcla(datos[:mitad])
    derecha = mezcla(datos[mitad:])
    return mezcla_ordenada(izquierda, derecha)
