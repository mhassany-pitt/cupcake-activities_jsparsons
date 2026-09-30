def centigrados_a_fahrenheit(temp):
    if temp < -273.15:
        raise ValueError("Temperatura por debajo del cero absoluto!")
    return temp*1.8+32
try:
    print(centigrados_a_fahrenheit(temp_a_convertir))
except ValueError:
    print("Temperatura configurada demasiado baja!")
