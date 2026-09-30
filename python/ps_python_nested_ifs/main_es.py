if am_o_pm == "am":
    if hora < 7:
        print("Todavia es de noche")
    else:
        print("Es de manana")
elif am_o_pm == "pm":
    if hora <= 5:
        print("Es de tarde")
    else:
        print("Es de noche")
