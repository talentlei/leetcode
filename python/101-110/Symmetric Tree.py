    def isMirror(self,p,q):
        if p==None and q==None:
            return True
        if p==None or q==None:
            return False
        return q.val==p.val and self.isMirror(p.left,q.right) and self.isMirror(p.right,q.left)
    # @param root, a tree node
    # @return a boolean
    def isSymmetric(self, root):
        if root==None:
            return True
        return self.isMirror(root.left,root.right)
