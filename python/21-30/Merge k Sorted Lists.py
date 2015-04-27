    
    def mergeTwoLists(self, l1, l2):
        if not l1:
            return l2
        if not l2:
            return l1
        su = ListNode(0)
        head = su
        while l1!=None and l2!=None:
            if l1.val <l2.val:
                head.next = l1
                l1 = l1.next
            else:
                head.next = l2
                l2 =l2.next
            head = head.next
            head.next=None
        if l1!=None:
            head.next = l1
        else:
            head.next = l2
        return su.next
    # @param {ListNode[]} lists
    # @return {ListNode}
    def mergeKLists(self, lists):
        if lists==None or len(lists)==0:
            return None
        if len(lists)==1:
            return lists[0]
        size= len(lists)
        l1 = self.mergeKLists(lists[:size//2])
        l2 = self.mergeKLists(lists[size//2:])
        return self.mergeTwoLists(l1,l2)
