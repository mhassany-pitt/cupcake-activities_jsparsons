num = 50
list = []
list2= []
list3= []
for i in range(1, num + 1):
        if i % 2 == 0 and i % 5 == 0:
                list.append(i)
        elif i % 2 == 0:
                list2.append(i)
        elif i % 5 == 0:
                list3.append(i)
print("divisible by only 2:")
print(list)
print("divisible by only 5:")
print(list2)
print("divisible by 2 & 5:")
print(list3)
