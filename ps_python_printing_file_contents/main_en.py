try:
file_to_read = open(filename, "r")
row = file_to_read.readline()
while row != "":
print(row)
row = file_to_read.readline()
file_to_read.close()
except OSError:
print("Error reading the file. The program execution ends.")
