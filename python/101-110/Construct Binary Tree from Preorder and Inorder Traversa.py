    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def subbuildTree(self, preorder, inorder,pbegin,pend,ibegin,iend):
        if pbegin-pend==0:
            return None
        val = preorder[pbegin]
        index = inorder.index(val)
        lsize = index-ibegin
        cnode = TreeNode(val)
        cnode.left = self.subbuildTree(preorder,inorder,pbegin+1,pbegin+lsize+1,ibegin,index)
        cnode.right = self.subbuildTree(preorder,inorder,pbegin+lsize+1,pend,index+1,iend)
        return cnode
        
    def buildTree(self,preorder,inorder):
        return self.subbuildTree(preorder,inorder,0,len(preorder),0,len(inorder))
