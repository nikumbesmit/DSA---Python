# Leetcode - 19. Remove Nth Node From End of List

class Solution:
    def removeNthFromEnd(self, head) :
        if not head :
            return None

        slow = fast = head
        count = 0

        while count < n :
            fast = fast.next
            count += 1

        if fast is None :
            return head.next

        while fast and fast.next :
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next

        return head
