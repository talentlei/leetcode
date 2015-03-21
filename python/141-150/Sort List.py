class Solution:
    def merge(self,l1,l2):
        if l1==None:
            return l2
        elif l2==None:
            return l1
        p1,p2=l1,l2
        result = ListNode(0)
        cur = result
        while p1!=None and p2!=None:
            if p1.val<p2.val:
                cur.next=p1
                p1=p1.next
            else:
                cur.next=p2
                p2=p2.next
            cur=cur.next
        if p1!=None:
            cur.next=p1
        if p2!=None:
            cur.next=p2
        return result.next
    def mergesort(self,head,size):
        if size<2:
            return head
        l1 = head
        p=head
        for i in range(size//2-1):
            p=p.next
        l2=p.next
        p.next=None
        r1 = self.mergesort(l1,size//2)
        r2 = self.mergesort(l2,size-size//2)
        return self.merge(r1,r2)
    # @param head, a ListNode
    # @return a ListNode
    def sortList(self, head):
        size=0
        p = head
        while p!=None:
            size+=1
            p=p.next
        if size <2:
            return head
        return self.mergesort(head,size)
        
