# Leetcode - 234. Palindrome Linked List
from __future__ import annotations

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def is_palindrome(head: ListNode | None) -> bool:
    if not head or not head.next:
        return True

    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    curr = slow
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    first, second = head, prev
    while second:  
        if first.val != second.val:
            return False
        first = first.next
        second = second.next

    return True


def create_linked_list(arr: list[int]) -> ListNode | None:
    
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head


user_input = input("Enter space-separated integers: ").strip()

if user_input:
    values = list(map(int, user_input.split()))
else:
    values = []

head = create_linked_list(values)

result = is_palindrome(head)
print(f"Is Palindrome Linked List: {result}")
