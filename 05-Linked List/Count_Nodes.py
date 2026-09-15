# Counts no. of Nodes in given Linked List

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

def print_ll(head):
    elements = []
    curr = head
    while curr:
        elements.append(str(curr.data))
        curr = curr.next
    print(" -> ".join(elements))

def count_nodes(head) :
    count = 0

    curr = head
    while curr :
        count += 1
        curr = curr.next

    return count


raw_values = input("Enter linked list elements separated by space (or press Enter if empty): ").strip()
arr = [int(val) for val in raw_values.split()] if raw_values else []

head = arr_to_ll(arr)
print_ll(head)
print(f"No. of Nodes in LinkedList = {count_nodes(head)}")
