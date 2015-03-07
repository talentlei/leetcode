    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        if root==None:
            return False
        if root.left==None and root.right==None:
            if sum==root.val:
                return True
            else:
                return False
        lh,rh = False,False
        if root.left==None:
            return self.hasPathSum(root.right, sum-root.val)
        elif root.right==None:
            return  self.hasPathSum(root.left, sum-root.val)
        return self.hasPathSum(root.left, sum-root.val) or self.hasPathSum(root.right, sum-root.val)
