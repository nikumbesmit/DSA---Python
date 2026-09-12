# Insert an element at any given position in a LinkedList

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

def insert_at_any_positon(head, x, pos) :

    if pos < 1 :
        raise IndexError("Position cannot be negative.")

    new_node = Node(x)

    # case 1 : Insert at beginning
    if pos == 1 :
        new_node.next = head
        return new_node

    # case 2 : Traverse to the node just before the target position
    curr = head
    for _ in range(pos-2) :
        if curr is None :
            raise IndexError("Position is out of bounds.")
        curr = curr.next

    new_node.next = curr.next
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
x = int(input("Enter the value x to insert : "))
pos = int(input("Enter the position where you want to insert insert : "))

try :
    head = insert_at_any_positon(head,x,pos)
    print("Modified Linked List: ", end="")
    print_ll(head)

except IndexError as e :
    print(f"Error : {e}")
