    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        if root==None:
            return 0
        lh = self.minDepth(root.left)
        rh = self.minDepth(root.right)
        if lh==0:
            return rh+1
        elif rh==0:
            return lh+1
        return min(lh,rh)+1
