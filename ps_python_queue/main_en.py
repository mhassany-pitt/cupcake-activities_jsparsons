def circle(k,name_list):
    q = Queue()
    if not q.is_empty():
        for i in range(len(name_list)):
            q.enqueue(name_list[i])
        i = 1
        while q.size()!=1:
            temp=q.dequeue()
            if i != k+1:
                q.enqueue(temp)
            else:
                i = 0
            i += 1
    else:
        return ('the list is empty!')
    return q.dequeue()
