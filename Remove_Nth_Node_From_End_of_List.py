 def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if head == None:
            return None 
        dummy = ListNode(0)
        dummy.next = head
        first = second = dummy
        for i in range(n): 
            first = first.next
            
        while first and first.next:
            first = first.next
            second = second.next
            
        second.next = second.next.next
        return dummy.next
