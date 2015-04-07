    def reverse(self,nums,start,end):
        while start<end:
            temp=nums[start]
            nums[start]=nums[end]
            nums[end]=temp
            start+=1
            end-=1
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        size=len(nums)
        k=k%size
        if size<2 or k==0:
            return 
        self.reverse(nums,0,size-1)
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,size-1)
