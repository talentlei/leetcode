
/**
  runtime: 72ms
  error : 1
*/
class Solution {
public:
    vector<vector<int>> fourSum(vector<int>& nums, int target) {
        vector<vector<int> > res;
        int size = nums.size();
        if(size<4) return res;
        sort(nums.begin(),nums.end());
        for(int i=0; i<nums.size()-3; i++){
            for(int j=i+1; j<nums.size()-2; j++){
                int beg = j+1,end= nums.size()-1;
                int sum = target-nums[i]-nums[j];
                while(beg<end){
                    // if(sum<nums[beg]) break;  //error 1
                    int temp = nums[beg]+nums[end];
                    if(temp ==sum){
                        vector<int> one; 
                        one.push_back(nums[i]);
                        one.push_back(nums[j]);
                        one.push_back(nums[beg]);
                        one.push_back(nums[end]);
                        res.push_back(one);
                        do{
                            beg++;
                        }while(beg<end&&nums[beg]==nums[beg-1]);
                        do{
                            end--;
                        }
                        while(beg<end&&nums[end]==nums[end+1]);
                    }
                    else if(temp<sum) 
                        beg++;
                    else end--;
                }while(j+1<nums.size()-2&&nums[j]==nums[j+1]) j++;
            }while(i+1<nums.size()-3&&nums[i]==nums[i+1]) i++;
            
        }return res;
    }
};
