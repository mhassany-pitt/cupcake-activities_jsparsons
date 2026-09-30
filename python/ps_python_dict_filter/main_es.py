circulos = {"azul": 8, "rojo": 5, "gris": 7}
for circulo in circulos.items():
    if(circulo[1] > 5):
        print("Circulo ",circulo[0], " es mayor que", 5)
