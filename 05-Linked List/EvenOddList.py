# Leetcode - 328. Odd Even Linked List

class LinkedList :

    def OddEvenList(self,head) :
        if not head :
            return None 

        odd = head 
        even = head.next
        even_head = even

        while even and even.next :
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = even_head

        return head
