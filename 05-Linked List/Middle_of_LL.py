# Leetcode - 876. Middle of the Linked List

from __future__ import annotations

class Node :
    def __init__(self,data):
        self.data = data
        self.next = None

def Arr_to_DLL(arr: list[int]) -> Node | None:
    if not arr :
        return None

    curr = head = Node(arr[0])

    for val in arr[1:] :
        curr.next = Node(val)
        curr = curr.next

    return head

def middleNode(head: Node | None) -> Node | None:
    slow = head 
    fast = head 

    while fast and fast.next :
        slow = slow.next
        fast = fast.next.next

    return slow


def print_DLL(head: Node | None) -> None:
    elements = []
    curr = head
    while curr:
        elements.append(str(curr.data))
        curr = curr.next
    print(" -> ".join(elements))


raw_values = input("Enter linked list elements separated by space (or press Enter if empty): ").strip()
arr = [int(val) for val in raw_values.split()] if raw_values else []

if arr:
    head = Arr_to_DLL(arr)
    print("The Linked List is : ", end = "")
    print_DLL(head)

    mid = middleNode(head)
    print("The Middle Node of Linked List is : ", end = "")
    print_DLL(mid)

else:
    print("Array is empty!") 
