    def combinationSum2(self, candidates, target):
        ans=[]
        candidates.sort() 
        for ii,elem in enumerate(candidates):
            if target>elem:
                subSet=self.combinationSum2(candidates[ii+1:],target-elem) # need to update the candidates list to avoid dublicates
                if subSet:
                    ans+=[[elem]+lis for lis in subSet]
            elif target==elem:
                ans+=[[elem]]
            else:
                break
        tans=[]
        for con in ans:
            if con not in tans:
                tans.append(con)
        return tans
