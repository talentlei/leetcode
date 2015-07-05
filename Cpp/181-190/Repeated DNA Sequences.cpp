class Solution {
public:
/**
 *  暴力方法: tle
 * 
 */ 
vector<string> findRepeatedDnaSequences(string s) {
        vector<string> res;
        if(s.size()<20) return res;
        unordered_set<string> model;
        for(int i=0; i+20<=s.size(); i++){
            string p = s.substr(i,10);
            if(model.find(p)!=model.end())
                continue;
            for(int j=i+10; j+10<=s.size(); j+=1){
                if(s.substr(j,10)==p){
                    model.insert(p);
                    res.push_back(p);
                    break;
                }
            }
        }
        return res;
    }
 /*
        将字符串hash到数字
 */
 vector<string> findRepeatedDnaSequences(string s) {
         vector<string> res;
         if(s.size()<10) return res;
         unordered_set<unsigned int> mySet;
         unordered_set<unsigned int> visited;
         int i=0;
         unsigned int temp=0;
         while(i<9){
                 temp=temp<<3|s[i]&0X07;
                 i++;
         }
         while(i<s.size()){
                 temp = temp<<3&0X03FFFFFFF|s[i]&0X07;
                 if(mySet.find(temp)!=mySet.end()){
                        if(visited.find(temp)==visited.end()){
                                res.push_back(s.substr(i-9,10));
                                visited.insert(temp);
                        }
                 }
                else mySet.insert(temp);
                i++;
         }
         return res;
 }
 /*
        字符串加入到hash
        MLE
 */
  vector<string> findRepeatedDnaSequences(string s) {
         vector<string> res;
         if(s.size()<10) return res;
         unordered_map<string,int> myMap;
         int i=0;
         while(i+10<=s.size()){
                string word = s.substr(i,i+10);
                if(myMap.count(word)==1)
                        res.push_back(word);
                myMap[word]++;
         }
         return res;
 }
};
