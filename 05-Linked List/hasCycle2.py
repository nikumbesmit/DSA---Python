# Leetcode - 142. Linked List Cycle II

class Solution:
    def detectCycle(self, head) :
        if not head or not head.next :
            return None
        
        slow = fast = head

        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next

            if slow == fast :
                slow = head
        
                while slow != fast :
                    slow = slow.next
                    fast = fast.next
                
                return slow
        
        return None 
