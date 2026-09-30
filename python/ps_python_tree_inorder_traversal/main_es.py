def recorrido_inorden(self, raiz):
    res = []
    if raiz:
        res = self.recorrido_inorden(raiz.izquierda)
        res.append(raiz.dato)
        res = res + self.recorrido_inorden(raiz.derecha)
    return res
