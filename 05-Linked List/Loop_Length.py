# Determine whether the Linked List contains cycle or not...if yes then count no. of nodes in the cycle

class Cycle :

    def CountNodesInLoops(self,head) :

        if not head or not head.next :
            return 0

        slow = fast = head  

        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next

            if slow == fast :
                return self.CountLoopLength(slow)

        return 0

    def CountLoopLength(self,meeting_point) :
        curr = meeting_point
        count = 1

        while curr.next != meeting_point :
            count += 1
            curr = curr.next

        return count
