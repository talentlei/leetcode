    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def rotateRight(self, head, k):
        if not head or k==0 :
            return head
        n=0
        p = head
        while p!=None :
            p=p.next
            n+=1
        k = k%n
        if k==0:
            return head
        fast= head
        for i in range(0,n-k-1):
            fast=fast.next
        temphead = fast.next
        fast.next = None
        fast = temphead
        while fast.next!=None:
            fast = fast.next
        fast.next=head
        return temphead
