def centigrade_to_fahrenheit(temp):
    if temp < -273.15:
        raise ValueError("Temperature below absolute zero!")
    return temp*1.8+32
try:
    print(centigrade_to_fahrenheit(temp_to_convert))
except ValueError:
    print("Temperature set impossibly low!")
