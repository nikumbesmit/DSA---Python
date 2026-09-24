# Leetcode - 141. Linked List Cycle

from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    @staticmethod
    def Arr_to_LL(arr) :
        if not arr : return None

        curr = head = ListNode(arr[0])
        for val in arr[1 : ] :
            curr.next = ListNode(val)
            curr = curr.next

        return head 

    @staticmethod
    def print_LL(head) :
        elements = []
        curr = head
        visited = set()

        while curr :
            if curr in visited :
                elements.append(f"{curr.val} (cycle back to {curr.val})")
                break
            visited.add(curr)
            elements.append(str(curr.val))
            curr = curr.next

        print(" -> ".join(elements))

class LLCycle :

    def hasCycle(self,head : Optional[ListNode]) -> bool :

        if not head or not head.next :
            return False

        slow = fast = head

        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next

            if slow == fast :
                return True

        return False

if __name__ == "__main__" :
    user_input = input("Enter LL elements separated by spaces: ").strip()

    if user_input:
        Linked_List = [int(x) for x in user_input.split()]
        head = ListNode.Arr_to_LL(Linked_List)

        print("Linked List : ", end = "")
        ListNode.print_LL(head)

        cycle_checker = LLCycle()
        print(f"\nDoes the linked list have cycle : {cycle_checker.hasCycle(head)}")

        if head and head.next:
            curr = head
            while curr.next:
                curr = curr.next
            curr.next = head  

            print("\nAfter manually connecting tail to head:")
            print(f"Does the linked list have a cycle? {cycle_checker.hasCycle(head)}")


    else:
        print("Linked List is empty!") 
