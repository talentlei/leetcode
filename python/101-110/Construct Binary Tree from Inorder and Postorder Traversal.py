    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def subbuildTree(self, postorder, inorder,pbegin,pend,ibegin,iend):
        if pbegin-pend==0:
            return None
        val = postorder[pend-1]
        index = inorder.index(val)
        lsize = index-ibegin
        cnode = TreeNode(val)
        cnode.left = self.subbuildTree(postorder,inorder,pbegin,pbegin+lsize,ibegin,index)
        cnode.right = self.subbuildTree(postorder,inorder,pbegin+lsize,pend-1,index+1,iend)
        return cnode
        
    def buildTree(self,inorder,postorder):
        return self.subbuildTree(postorder,inorder,0,len(postorder),0,len(inorder))
