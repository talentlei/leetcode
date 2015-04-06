# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def rightSideView(self, root):
        if root==None:
            return []
        res=[]
        stack=[root]
        tmp=[]
        while len(stack)>0:
            p=None
            while len(stack)>0:
                p=stack[0]
                if p.left!=None:
                    tmp.append(p.left)
                if p.right!=None:
                    tmp.append(p.right)
                del stack[0]
            res.append(p.val)
            stack=tmp[:]
            tmp=[]
        return res
                    
                    
            
