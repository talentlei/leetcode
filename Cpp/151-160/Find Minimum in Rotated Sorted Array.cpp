
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
        int beg = 0,end = nums.size()-1;
        while(beg<end){
          int mid = beg+(end-beg)/2;
          if(nums[mid]>nums[end])
            beg = mid+1;
          else if(nums[mid]<nums[end])
            end = mid;
          else end--;
        }
        return nums[beg];
    }
};
