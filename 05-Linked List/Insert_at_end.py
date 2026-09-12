# Insertion an element at the end of a LinkedList

class Node :
    def __init__(self,data):
        self.data = data
        self.next = None

def arr_to_ll(arr) :
    if not arr :
        return None

    head = curr = Node(arr[0])
    for val in arr[1:] :
        curr.next = Node(val)
        curr = curr.next

    return head 

def insert_at_end(head : Node, x : int) -> Node :
    new_node = Node(x)

    if not head :
        return new_node
    
    curr = head
    while curr.next :
        curr = curr.next 

    curr.next = new_node

    return head

def print_ll(head):
    elements = []
    curr = head
    while curr:
        elements.append(str(curr.data))
        curr = curr.next
    print(" -> ".join(elements))


raw_values = input("Enter linked list elements separated by space (or press Enter if empty): ").strip()
arr = [int(val) for val in raw_values.split()] if raw_values else []

head = arr_to_ll(arr)
x = int(input("Enter the value x to insert at the end: "))

head = insert_at_end(head, x)

print("Modified Linked List: ", end="")
print_ll(head)
