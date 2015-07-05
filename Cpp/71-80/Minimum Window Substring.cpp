    string minWindow(string s, string t) {
        if(s.size()==0||t.size()==0) return "";
        unordered_map<char,int> myMap;
        unordered_map<char,int> temp;
        foreach(auto ch: t)
            myMap[ch]++;
        string res="";
        int num = 0;
        int beg=0,end=0;
        while(end<s.size()){
            char ch = s[end];
            if(myMap.find(ch)==myMap.end()){
                end++;
                continue;
            }
            if(temp[ch]+1==myMap[ch])
                num++;
            if(num==myMap.size()){
                if(res==""||res.size()>end-beg+1)
                    res = s.substr(beg,end-beg+1);
                if(myMap.find(s[beg])!=myMap.end()&&temp[s[beg]]==myMap[s[beg]])
                    num--;
                beg++;
            }else end++;
        }return res;
    }  
  
