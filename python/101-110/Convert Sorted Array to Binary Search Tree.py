    # @param num, a list of integers
    # @return a tree node
    def sortedArrayToBST(self, num):
        if len(num)==0:
            return None
        mid = len(num)//2
        cur = TreeNode(num[mid])
        cur.left = self.sortedArrayToBST(num[0:mid])
        cur.right = self.sortedArrayToBST(num[mid+1:])
        return cur
