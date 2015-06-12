class TrieNode {
public:
    // Initialize your data structure here.
    char val;
    bool istail;
    vector<TrieNode*> next;
    TrieNode(char c) {
        val = c;
        istail = false;
    }
    TrieNode() {
        val='/';
        istail = false;
    }
};

class Solution {
public:
    Solution() {
        root = new TrieNode();
    }
    // Inserts a word into the trie.
    void insert(string s) {
        TrieNode* cur = root;
        for(int i=0;i<s.size();i++){
            bool isFound=false;
            for(int j=0; j<(cur->next).size();j++){
                if((cur->next)[j]->val==s[i]){
                    cur = (cur->next)[j];
                    isFound = true;
                    break;
                }
            }
            if(!isFound){
                while(i<s.size()){
                    TrieNode* node = new TrieNode(s[i]);
                    cur->next.push_back(node);
                    cur = node;
                    i++;
                }
            }
        }
        cur->istail =true;
    }

    void addResult(vector<char>& path){
        string str = "";
        for(int i=0; i< path.size(); i++)
            str+=path[i];
        mySet.insert(str);
    }
    void DFS(vector<vector<char>>& board, vector<string>& words,vector<vector<int>>& base,int i,int j,TrieNode* cur,vector<char> & path){
        int id,col,row;
        row = board.size();
        col = board[0].size();
        bool isFound = false;
        for(id=0; id<(cur->next).size(); id++){
                if((cur->next)[id]->val==board[i][j]){
                    cur = (cur->next)[id];
                    isFound = true;
                    break;
                }
        }
        if(!isFound)
            return;
        //match
        base[i][j]=1;
        path.push_back(board[i][j]);
        if(cur->istail)
            addResult(path);
        
        int dx[] = {-1,0,1,0};
        int dy[] = {0,-1,0,1};
        int x,y;
        for(int k=0; k<4; k++){
            x = dx[k]+i;
            y = dy[k]+j;
            if(x>=0 && x<row&& y>=0 && y<col && base[x][y]==0){
                TrieNode * tmp = cur;
                DFS(board,words,base,x,y,tmp,path);
            }
        }
        base[i][j] = 0;
        path.pop_back();
    }
    //method 1
    vector<string> findWords(vector<vector<char>>& board, vector<string>& words) {
        vector<string> res;
        if(words.size()==0|| board.size()==0 || board[0].size()==0)
            return res;
        int row,col;
        row = board.size();
        col = board[0].size();
        vector<vector<int> > base(row,vector<int>(col,0));
        vector<char> path;
        for(int i=0; i<words.size();i++)
            insert(words[i]);
        for(int i=0; i<row; i++)
            for(int j=0; j<col; j++)
                DFS(board,words,base,i,j,root,path);
        res.assign(mySet.begin(),mySet.end());
        return res;
    }

private:
    TrieNode* root;
    unordered_set<string> mySet;
};
