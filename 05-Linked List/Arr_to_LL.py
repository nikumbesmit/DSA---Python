# Convert an Given array into linked list

class Node :
    def __init__(self,data):
        self.data = data
        self.next = None

def Arr_to_LL(arr) :
    if not arr : return None

    curr = head = Node(arr[0])
    for val in arr[1 : ] :
        curr.next = Node(val)
        curr = curr.next

    return head 

def print_LL(head) :
    elements = []
    curr = head

    while curr :
        elements.append(str(curr.data))
        curr = curr.next
    print(" -> ".join(elements))

raw_values = input("Enter integer array elements separated by space : ")
arr = [int(x) for x in raw_values.split()]

if arr:
    head = Arr_to_LL(arr)
    print("The converted Linked List : ", end = "")
    print_LL(head)
else:
    print("Array is empty!") 
