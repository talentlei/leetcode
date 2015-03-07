    def sortedArrayToBST(self, num):
        if len(num)==0:
            return None
        mid = len(num)//2
        cur = TreeNode(num[mid])
        cur.left = self.sortedArrayToBST(num[0:mid])
        cur.right = self.sortedArrayToBST(num[mid+1:])
        return cur
    # @param head, a list node
    # @return a tree node
    def sortedListToBST(self, head):
        num=[]
        if head==None:
            return None
        while head!=None:
            num.append(head.val)
            head=head.next
        return self.sortedArrayToBST(num)
