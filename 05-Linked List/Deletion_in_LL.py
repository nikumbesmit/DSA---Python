# Delete a given node in LinkedList

class Node :
    def __init__(self,data):
        self.data = data
        self.next = None


# If node is given
def delete_node(node) :
    if node is None or node.next is None:
        raise ValueError("Cannot delete the last node or a None node with this method.")
    node.data = node.next.data
    node.next = node.next.next 


def delete_at_beginning(head) :
    if head is None :
        return None

    return head.next

def delete_at_end(head) :
    if head is None or head.next is None :
        return None

    curr = head
    while curr.next.next :
        curr = curr.next

    curr.next = None
    return head

def delete_at_anyPosition(head,pos) :
    if head is None or pos < 1 :
        return head

    if pos == 1 :
        return head.next

    curr = head
    for _ in range(pos-2) :
        if curr.next is None :
            return head
        curr = curr.next 

    if curr.next is not None :  
        curr.next = curr.next.next

    return head


