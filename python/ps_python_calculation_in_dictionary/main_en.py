for item in studentdict.items():
    name=item[0]
    scores=item[1]
    total=0
    for score in scores:
        total+=score
    ave = total/len(scores)
    print("The average score of",name, "is",ave)
