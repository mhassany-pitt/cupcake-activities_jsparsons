def traverse_list(doubly_linked_list):
    current = doubly_linked_list.head
    while current:
        print(current.data, end=" ")
        last = current
        current = current.next
    while last:
        print(last.data, end=" ")
        last = last.prev
