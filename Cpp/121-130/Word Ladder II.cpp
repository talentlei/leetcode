class Solution {
public:
    //not accept now
    vector<vector<string> > res;
    void createResult(unordered_map<string,int> myMap,unordered_map<string,vector<string> >& record,string beginWord,string endWord,vector<string> & one,string next){
        one.push_back(next);
      if(one.size()==myMap[end]){
            if(next==beginWord ){
              vector<string> vec(one.begin,one.end());
              reverse(vec.begin(),vec.end());
              res.push_back(vec);
            }
            one.pop_back();
            return ;
        }
      vector<string>::iterator iter;
      for(iter=record[next].begin(); iter!=record[next].end();iter++){
        createResult(myMap,record,beginWord,endWord,one,*iter);
      }
      one.pop_back();
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
        unordered_map<string,vector<string> > record;
        Queue.push(beginWord);
        vector<string> vec;
        record[beginWord]=vec;
        myMap[beginWord]=1;
        
        while(!Queue.empty()&&(myMap.find(endWord)==myMap.end()||myMap[endWord]>myMap[Queue.front()])){
          string word = Queue.front();
          string temp = word;
          Queue.pop();
          for(int i=0; i<temp.size();i++){
            for(int j=0; j<26; j++){
              temp[i] = 'a'+j;
              if(wordDict.count(temp)!=0 ){
                if(myMap.find(temp)==myMap.end()){
                  myMap[temp] = myMap[word]+1;
                  Queue.push(temp);
                  vector<string> vect(1,temp);
                  record[temp]=vect;
                  }
                else{
                  record[temp].push_back(word);
                }
              }
            }
          }
        }
        if(myMap.count(endWord)!=0){
          vector<string> one;
          createResult(myMap,record,beginWord,endWord,one,endWord);
        }
        return res;
    }
};
