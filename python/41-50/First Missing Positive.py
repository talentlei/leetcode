    def firstMissingPositive(self, nums):
        for i in xrange(len(nums)):
            while nums[i]<=len(nums) and nums[i]>0 and nums[i]!=nums[nums[i]-1]:
                nums[nums[i]-1],nums[i]= nums[i],nums[nums[i]-1]
                
        i=0
        while i<len(nums) and i+1==nums[i]:
            i+=1
        return i+1
