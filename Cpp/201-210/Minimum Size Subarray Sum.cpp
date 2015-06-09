int minSubArrayLen(int s, vector<int>& nums) {
        int size = nums.size();
        int res=0,sum=0,beg=0,end=0;
        while(beg<size){
            while(end<size && sum<s ){
                sum+=nums[end];
                end++;
            }
            if((sum>=s)&&(res==0||end-beg<res))
                res = end-beg;
            sum-=nums[beg];
            beg++;
        }
        return res;
    }
