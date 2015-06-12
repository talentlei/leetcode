class Solution {
public:
    int rob(vector<int>& nums) {
        int size = nums.size();
        if(size<=0)
            return 0;
        if(size==1)
            return nums[0];
        int res=0;
        int base[size];
        memset(base,0,sizeof(base));
        base[0] = nums[0];
        base[1] = nums[0];
        for(int i=2; i< size;i++)
            base[i] = max(base[i-1],base[i-2]+nums[i]);
        res = base[size-1];
        if(base[size-1]!=base[size-2])
            res = base[size-2];
            
        memset(base,0,sizeof(base));
        base[0] = 0;
        base[1] = nums[1];
        for(int i=2; i< size;i++)
            base[i] = max(base[i-1],base[i-2]+nums[i]);
        if(base[size-1]>res)
            res = base[size-1];
        return res;
    }
};
