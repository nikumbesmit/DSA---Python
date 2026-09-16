# Delete an Node in given Doubly LinkedList

class Node :
    def __init__(self,data) :
        self.data = data
        self.next = None
        self.prev = None

def Delete(head,pos) :
    if head is None or pos < 1 :
        return head

    if pos == 1 :
        new_head = head.next
        if new_head is not None :
            new_head.prev = None
        return new_head

    curr = head 
    for _ in range(pos-1) :
        curr = curr.next

        if curr is None :
            return head

    if curr.prev is not None :
        curr.prev.next = curr.next

    if curr.next is not None :
        curr.next.prev = curr.prev

    return head
