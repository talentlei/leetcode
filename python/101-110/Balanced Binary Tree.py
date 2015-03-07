    def subIsBalanced(self,root):
        if root==None:
            return True,0
        lb,lh =self.subIsBalanced(root.left)
        rb,rh =self.subIsBalanced(root.right)
        if lb and rb and abs(lh-rh)<=1:
            return True,max(lh,rh)+1
        return False,0
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        isBa,th = self.subIsBalanced(root)
        return isBa
