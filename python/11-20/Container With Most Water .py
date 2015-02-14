class Solution:
    # @return an integer
    def maxArea(self, height):
        left,right = 0,len(height)-1
        MAX,temp = 0,0
        while left<right:
            if height[left] < height[right]:
                shorter = height[left]
                left+=1
            else:
                shorter = height[right]
                right-=1
            temp = (right-left+1)*shorter
            if temp > MAX:
                MAX=temp
        return MAX
