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
    
};
