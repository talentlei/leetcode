/**
  runtime: 8ms
  error: 2   not consider begin with 0. such as "00";
*/

bool cmp(string a, string b){
  string str1 = a+b;
  string str2 = b+a;
  return strcmp(str1.c_str(),str2.c_str())>0;
}
class Solution {
public:
    string largestNumber(vector<int>& nums) {
      vector<string> strs(nums.size(),"");
      stringstream stream;
      for(int i=0; i<nums.size(); i++){
        stream<<nums[i];
        strs[i]= stream.str();
        stream.str("");
      }
      sort(strs.begin(),strs.end(),cmp);
      string res = "";
      for(int i=0; i<strs.size();i++)
        res += strs[i];
      int beg=0;
      while(beg<res.size()&& res[beg]=='0')
        beg++;
      if(beg==res.size())
        beg--;
      return res.substr(beg);
    }
   
};
