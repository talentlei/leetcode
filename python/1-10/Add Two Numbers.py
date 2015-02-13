# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        r=0
        array=[]
        while l1!=None or l2!=None:
            if l1==None:
                num1=0 
            else :
                num1=l1.val
            if l2==None:
                num2=0 
            else:
                num2=l2.val
            sum = num1+num2+r
            r = sum/10
            data = sum%10
            array.append(data)
            if l1!=None:
                l1=l1.next
            if l2!=None:
                l2=l2.next
        if r!=0:
            array.append(1)
        head=ListNode(0)
        p=head
        for data in array:
            temp=ListNode(data)
            p.next=temp
            p=temp
        return head.next
