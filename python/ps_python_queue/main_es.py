def circulo(k, lista_nombres):
    q = Cola()
    if not q.is_empty():
        for i in range(len(lista_nombres)):
            q.enqueue(lista_nombres[i])
        i = 1
        while q.size() != 1:
            temp = q.dequeue()
            if i != k+1:
                q.enqueue(temp)
            else:
                i = 0
            i += 1
    else:
        return ('la lista esta vacia!')
    return q.dequeue()
