    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head==None or head.next==None:
            return False
        slow,fast=head,head.next.next
        while fast!=None :
            if fast==slow:
                return True
            slow=slow.next
            if fast.next==None:
                break
            fast=fast.next.next
        return False
