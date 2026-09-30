index_min = 0
index_max = 0
for index in range(1, len(num_list)):
    if num_list[index] < num_list[index_min]:
        index_min = index
    if num_list[index] > num_list[index_max]:
        index_max = index
print(index_min, index_max)
