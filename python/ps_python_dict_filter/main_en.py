circles = {"blue": 8, "red": 5, "grey": 7}
for circle in circles.items():
    if(circle[1] > 5):
        print(circle[0], "circle is larger than", 5)
