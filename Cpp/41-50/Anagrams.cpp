/**
  runtime:56ms
  error: understand error.

*/
class Solution {
public:
    vector<string> anagrams(vector<string>& strs) {
        unordered_map<string,vector<string> > myMap;
        for(int i=0; i<strs.size(); i++){
            string word = strs[i];
            sort(word.begin(),word.end());
            if(myMap.find(word)==myMap.end()){
                vector<string> temp;
                temp.push_back(strs[i]);
                myMap[word]=temp;    
            }else myMap[word].push_back(strs[i]);
        }
        vector<string> res;
        for(unordered_map<string,vector<string> >::iterator iter= myMap.begin(); iter!=myMap.end(); iter++){
            if((iter->second).size()>1){
                res.insert(res.end(),(iter->second).begin(),(iter->second).end());
            }
        }
        return res;
    }
};
