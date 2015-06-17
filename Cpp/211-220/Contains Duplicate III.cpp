class Solution {
public:
    //method 1  o(min(k,t)n)time o(1)oro(n) space
    bool k_min(vector<int>& nums, int k, int t){
          int len = nums.size();
          long pi,pj,pt;
          pt = t;
          for(int i=0; i<len; i++){
            for(int j=i+1; j<=i+k&& j<len; j++){
              pi = nums[i];
              pj = nums[j];
              if(abs(pi-pj)<=pt)
                return true;
            }
          }
          return false;
    }
    bool t_min(vector<int>& nums, int k,int t) {
        set<int > myset;
        for(int i = 0; i < nums.size(); i++){
            if(i > k) myset.erase(nums[i-k-1]);
            for(int j=nums[i]-t; j<=nums[i]+t; j++)
              if(myset.count(j)!=0) return true;
            myset.insert(nums[i]);
        }
        return false;
    }
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
    if(k<t){
          return k_min(nums,k,t);
        }
    else{
        return t_min(nums,k,t);
      }
    }
    
    //method 2 o(n)time  o(n)time
    bool containsNearbyAlmostDuplicate(vector<int>& nums, int k, int t) {
        if(nums.size()<2|| k<1||t<0) return false;
        long mx = *max_element(nums.begin(),nums.end());
        long mn = *min_element(nums.begin(),nums.end());
        long bucket;
        long pt = t;
        map<long,int > record;
        for(int i=0; i<nums.size(); i++){
          bucket = ((nums[i])-mn)/(pt+1);
          if(record.count(bucket)!=0||record.count(bucket-1)!=0&&static_cast<long>(nums[i])-record[bucket-1]<=pt
            ||record.count(bucket+1)!=0&&record[bucket+1]-static_cast<long>(nums[i])<=pt)
              return true;
          if(record.size()>=k)
            record.erase((nums[i-k]-mn)/(pt+1));
          record.insert(make_pair(bucket,nums[i]));
        }
        return false;
    }
};
