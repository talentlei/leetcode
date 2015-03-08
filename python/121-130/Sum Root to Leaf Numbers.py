    sum=0
    def sub(self,root,num):
        value = num*10+root.val
        if root.left==None and root.right==None:
            self.sum+=value
            return
        if root.left!=None:
            self.sub(root.left,value)
        if root.right!=None:
            self.sub(root.right,value)
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
        if root==None:
            return 0
        self.sub(root,0)
        return self.sum
