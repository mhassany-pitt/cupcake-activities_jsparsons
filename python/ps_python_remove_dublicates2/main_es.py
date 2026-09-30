nueva_lista = []
for elemento in lista_original:
        if elemento not in nueva_lista:
                nueva_lista.append(elemento)
print("La lista original:", lista_original)
print("La nueva lista:", nueva_lista)
