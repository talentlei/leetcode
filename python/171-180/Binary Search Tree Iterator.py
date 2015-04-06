# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class BSTIterator:
    cur=None
    stack=[]
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.cur=root
        self.stack=[]
        

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        if self.cur!=None or len(self.stack)>0:
            return True
        else:
            False

    # @return an integer, the next smallest number
    def next(self):
        p=self.cur
        while p!=None:
            self.stack.append(p)
            p=p.left
            
        t=self.stack.pop()
        self.cur=t.right
        return t.val

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())
