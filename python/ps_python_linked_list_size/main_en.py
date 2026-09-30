def get_size(linked_list):
    count = 0
    temp = linked_list.head
    while temp:
        count = count + 1
        temp = temp.next
    return count
