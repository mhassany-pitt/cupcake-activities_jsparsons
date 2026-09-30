for item in dicc_estudiantes.items():
    nombre=item[0]
    notas=item[1]
    total=0
    for nota in notas:
        total+=nota
    promedio = total/len(notas)
    print("El promedio de",nombre, "es",promedio)
