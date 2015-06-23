class Solution {
public:
    //count sort
    void sortColors(vector<int>& nums) {
        vector<int > vec(3,0);
        for(int i=0; i<nums.size();i++)
          vec[nums[i]]++;
        int end = 0,i=0;
        for(int j=0;j<3;j++){
          end += vec[j];
          for(; i<end; i++)
            nums[i] = j;
        }
    }
};
