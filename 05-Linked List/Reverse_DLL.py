# Reversing an given DLL 

class Node :
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

def Arr_to_DLL(arr) :
    if not arr :
        return None

    head = None
    tail = None

    for val in arr :
        new_node = Node(val)

        if head is None :
            head = new_node
            tail = new_node
        else :
            tail.next = new_node
            new_node.prev = tail
            tail = new_node

    return head


def Reverse(head) :
    if head is None or head.next is None :
        return head

    curr = head
    new_head = None

    while curr is not None :
        new_head = curr
        curr.prev , curr.next = curr.next , curr.prev
        curr = curr.prev

    return new_head


def print_DLL(head):
    elements = []
    curr = head
    while curr:
        elements.append(str(curr.data))
        curr = curr.next
    print(" <-> ".join(elements))


raw_values = input("Enter linked list elements separated by space (or press Enter if empty): ").strip()
arr = [int(val) for val in raw_values.split()] if raw_values else []

if arr:
    head = Arr_to_DLL(arr)
    print("The Doubly Linked List is : ", end = "")
    print_DLL(head)

    new_head = Reverse(head)
    print("The Reversed Doubly Linked List is : ", end = "")
    print_DLL(new_head)

else:
    print("Array is empty!") 
