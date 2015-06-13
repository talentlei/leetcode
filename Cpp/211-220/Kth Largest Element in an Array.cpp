class Solution {
public:
    int findKthNum(vector<int>& nums,int k, int begin, int end){
        int x = nums[end];
        int slow = begin;
        for(int i=begin; i<=end; i++)
            if(nums[i]<x)
                swap(nums[i],nums[slow++]);
        swap(nums[end],nums[slow]);
        if(slow-begin+1 == k)
            return x;
        if(slow-begin+1 < k)
            return findKthNum(nums,k-slow+begin-1,slow+1,end);
        else
            return findKthNum(nums,k,begin,slow-1);
    }
    int findKthLargest(vector<int>& nums, int k) {
        // return findKthNum(nums,nums.size()-k+1,0,nums.size()-1);
        return findKthNum(nums,nums.size()-k+1,0,nums.size()-1);
    }
};
