def divisible_by(num):
        for i in range(1, num + 1):
                if i % 2 == 0 and i % 5 == 0:
                        print(i, "is divisible by 2 & 5")
                elif i % 5 == 0:
                        print(i, "is only divisible by 5")
                elif i % 2 == 0:
                        print(i, "is only divisible by 2")
                else:
                        print(i, "is not divisible by 2 nor 5")
divisible_by(100)
