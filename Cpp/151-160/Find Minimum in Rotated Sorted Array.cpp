
/*
    binary search method 
    o(lgn) time 
    o(1) space 
    run time : 4ms
    error :1   in line : while(beg<end)
*/
class Solution {
public:
    int findMin(vector<int>& nums) {
        if(nums.size()<2||nums[0]<nums[nums.size()-1])
          return nums[0];
        int beg = 0,end = nums.size()-1;
        while(beg<=end){
          int mid = beg+(end-beg)/2;
          if(nums[mid]>nums[mid+1])
            return nums[mid+1];
          else if(nums[mid]<nums[0])
            end = mid-1；
          else beg = mid+1;
        }
        return nums[beg];
    }
};
