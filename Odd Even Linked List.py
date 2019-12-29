 def oddEvenList(self, head: ListNode) -> ListNode:
        if not head: return head
        odd = head
        even = head.next
        evenlist = even
        while even != None and even.next != None:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next
        
        odd.next = evenlist
        return head
