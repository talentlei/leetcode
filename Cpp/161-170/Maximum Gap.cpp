/*
    error: 1, Max,Min init;  i use "int Max[size-1]={-1}"; this make Max ={-1,0,0,0...} rather than {-1,-1,-1...}
    runtime: 12ms
*/
class Solution {
public:
    int maximumGap(vector<int>& nums) {
        int size=nums.size();
        if(size<2) return 0;
        int maxe = *max_element(nums.begin(),nums.end());
        int mine = *min_element(nums.begin(),nums.end());
        int gap = (maxe-mine)/(size-1)+1;
        int Max[size-1] = {-1};
        int Min[size-1] = {maxe};
        for(int i=0; i<size; i++){
          if(nums[i]==maxe)
            continue;
          int BucketId = (nums[i]-mine)/gap;
          Max[BucketId] = max(Max[BucketId],nums[i]);
          Min[BucketId] = min(Min[BucketId],nums[i]);
        }
        int t=mine,res=0;
        for(int i=0; i<size-1; i++){
          if(Min[i] == maxe)
            continue;
          if(Min[i]-t>res)
            res = Min[i]-t;
          t = Max[i];
        }
        if(maxe-t>res)
          res = maxe-t;
        return res;
    }
    
};
