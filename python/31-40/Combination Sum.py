    def combinationSum(self, candidates, target):
        ans=[]
        candidates.sort() 
        for ii,elem in enumerate(candidates):
            if target>elem:
                subSet=self.combinationSum(candidates[ii:],target-elem) # need to update the candidates list to avoid dublicates
                if subSet:
                    ans+=[[elem]+lis for lis in subSet]
            elif target==elem:
                ans+=[[elem]]
            else:
                break
        return ans
