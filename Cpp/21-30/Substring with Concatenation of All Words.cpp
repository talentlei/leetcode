class Solution {
public:
    vector<int> findSubstring(string s, vector<string>& words) {
        vector<int > res;
        if(words.size()==0||s.size()==0)
            return res;
        unordered_map<string,int> mySet;
        unordered_map<string,int> wordsnum;
        for(int i=0; i<words.size(); i++)
            wordsnum[words[i]]++;
        int len = words[0].size();
        int num=0;
        for(int beg = 0; beg<len; beg++){
            int i = beg;
            int bpos;
            for(;i<s.size(); i+=len){
                string word = s.substr(i,len);
                if(words.find(word)==words.end())
                    mySet.clear();
                else{
                    if(mySet.find(word)==mySet.end()){
                        if(mySet.size()==0)
                            bpos = i;       
                        mySet.insert(word);
                        num++;
                    }
                    else if(mySet[word]<wordsnum[word]){
                        num++;
                        mySet[word]++;
                    }else{
                        string bw; 
                        while(bw = s.substr(bpos,len)!=word)
                            bpos
                    }
                        
                }
            }
        }
    }
};
