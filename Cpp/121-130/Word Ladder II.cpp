class Solution {
public:
    vector<vector<string> > res;
    void createResult(unordered_map<string,unordered_set<string> >& record,string endWord,int len,vector<string> & one,string beginWord){
      if(len==0){
            if(endWord==beginWord ){
              reverse(one.begin(),one.end());
              res.push_back(one);
            }
            return ;
        }
      unordered_set<string>::iterator iter;
      for(iter=record[endWord].begin(); iter!=record[endWord].end();iter++){
        one.push_back(*iter);
        createResult(record,*iter,len-1,one,beginWord);
        one.pop_back();
      }
      
    }
    //not be accepted now
    vector<vector<string>> findLadders(string beginWord, string endWord, unordered_set<string>& wordDict) {
        if(beginWord==endWord){
            vector<string> vec(1,beginWord);
            res.push_back(vec);
          return res;
        }
        wordDict.insert(beginWord);
        wordDict.insert(endWord);
        queue<string> Queue;
        unordered_map<string,int> myMap;
        unordered_map<string,unordered_set<string> > record;
        Queue.push(beginWord);
        unordered_set<string> vec;
        record.insert(make_pair(beginWord,vec));
        myMap[beginWord]=1;
        
        while(!Queue.empty()&&(myMap.count(endWord)==0||myMap[endWord]<=myMap[Queue.front()])){
          string word = Queue.front();
          string temp = word;
          Queue.pop();
          for(int i=0; i<temp.size();i++){
            char ch = temp[i];
            for(int j=0; j<26; j++){
              temp[i] = 'a'+j;
              if(wordDict.count(temp)!=0 ){
                if(myMap.count(temp)==0){
                  myMap[temp] = myMap[word]+1;
                  Queue.push(temp);
                  unordered_set<string> vec;
                  vec.insert(word);
                  record[temp]=vec;
                  }
                else{
                  record[temp].insert(word);
                }
              }
            }
            temp[i] = ch;
          }
        }
        if(myMap.count(endWord)==0)
          return res;
        vector<string> one;
        one.push_back(endWord);
        createResult(record,endWord,myMap[endWord]-1,one,beginWord);
        return res;
    }
};
