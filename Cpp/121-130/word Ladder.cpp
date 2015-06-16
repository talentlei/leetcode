class Solution {
public:
    int ladderLength(string beginWord, string endWord, unordered_set<string>& wordDict) {
        if(beginWord==endWord)
          return 1;
        wordDict.insert(beginWord);
        wordDict.insert(endWord);
        queue<string> Queue;
        unordered_map<string,int> myMap;
        Queue.push(beginWord);
        myMap[beginWord]=1;
        while(!Queue.empty()){
          string word = Queue.front();
          string temp = word;
          Queue.pop();
          for(int i=0; i<temp.size();i++){
            char ch = temp[i];
            for(int j=0; j<26; j++){
              temp[i] = 'a'+j;
              if(wordDict.count(temp)!=0 && myMap.count(temp)==0){
                myMap[temp] = myMap[word]+1;
                if(temp == endWord) return myMap[temp];
                Queue.push(temp);
              }
            }
            temp[i] = ch;
          }
        }
        return 0;
    }
};
