if am_or_pm == "am":
    if hour < 7:
        print("It is still night")
    else:
        print("It is morning")
elif am_or_pm == "pm":
    if hour <= 5:
        print("It is afternoon")
    else:
        print("It is evening")
