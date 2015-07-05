    string minWindow(string s, string t) {
        
    }  
  
   vector<int> findSubstring(string s, vector<string>& words) {
        vector<int > res;
        if(words.size()==0||s.size()==0)
            return res;
        unordered_map<string,int> mySet;
        unordered_map<string,int> wordsnum;
        for(int i=0; i<words.size(); i++)
            wordsnum[words[i]]++;
        int len = words[0].size();
        for(int beg = 0; beg<len; beg++){
            int num=0, i = beg, bpos;
            mySet.clear();                           // error 3: forget to clear mySet and num;
            for(;i+len<=s.size(); i+=len){           //error 2 i+len<s.size();
                string word = s.substr(i,len);
                if(wordsnum.find(word)==wordsnum.end()){
                    mySet.clear();
                    num=0;           //error 1: forget
                }
                else{
                    if(mySet.find(word)==mySet.end()){
                        if(mySet.size()==0)
                            bpos = i;       
                        mySet[word]++;
                        num++;
                    }
                    else if(mySet[word]<wordsnum[word]){
                        num++;
                        mySet[word]++;
                    }else{
                        string bw; 
                        while((bw = s.substr(bpos,len))!=word){
                            bpos+=len;
                            mySet[bw]--;
                            num--;
                        }
                        bpos+=len;
                    }
                    if(num==words.size())
                        res.push_back(bpos);
                }
            }
        }
        return res;
    }
