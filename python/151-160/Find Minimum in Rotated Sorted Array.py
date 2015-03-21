class Solution:
    # @param num, a list of integer
    # @return an integer
    def findMin(self, num):
        size=len(num)
        if size==0:
            return 0
        Min=num[0]
        low,high=0,size-1
        while low<=high:
            mid = low+high//2
            print low,high,mid
            if num[mid]<Min:
                Min=num[mid]
                if num[mid-1]<num[mid]:
                    high=mid-1
                else:
                    break
            else: 
                low=mid+1
        return Min
so=Solution()
data=[1,2,3]
print so.findMin(data)
