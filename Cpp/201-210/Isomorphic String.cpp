class Solution {
public:
    bool isIsomorphic(string s, string t) {
        map<char,char> myMap;
        map<char,char> RMap;
        int size = s.size();
        for(int i=0; i<size; i++){
            if((myMap.count(s[i])!=0&&myMap[s[i]]!=t[i]) ||(RMap.count(t[i])!=0&&RMap[t[i]]!=s[i]))
                    return false;
            else {
                myMap.insert(make_pair(s[i],t[i]));
                RMap.insert(make_pair(t[i],s[i]));  
            }
        }
        return true;
    }
};
