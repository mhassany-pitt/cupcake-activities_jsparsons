try:
    myfile=open(filename, "r")
    linenum=1
    for line in myfile:
        words = line.split()
        word=words[2]
        print("The third word in line",linenum,"is",word)
        linenum+=1
except OSError:
    print("Error reading the file.")
