    Max=0
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
        if root==None:
            return 0
        self.Max=root.val
        self.getMaxNum(root)
        return self.Max
    def getMaxNum(self,root):
        if root.left==None and root.right==None:
            if root.val>self.Max:
                self.Max=root.val
            return root.val
        value = root.val
        left,right=0,0
        if root.left!=None:
            left=self.getMaxNum(root.left)
        if root.right!=None:
            right=self.getMaxNum(root.right)
        tempmax=max(value,max(value+left,value+right))
        temp = max(tempmax,value+left+right)
        if temp>self.Max:
            self.Max=temp
        return tempmax
