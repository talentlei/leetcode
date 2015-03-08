    # @param head, a ListNode
    # @return a list node
    def detectCycle(self, head):
        if head==None:
            return None
        fast,slow=head,head
        entry=head
        while fast.next!=None:
            if fast.next.next==None:
                break
            fast=fast.next.next
            slow=slow.next
            if fast==slow:
                while slow!=entry:
                    slow=slow.next
                    entry=entry.next
                return entry
        return None
