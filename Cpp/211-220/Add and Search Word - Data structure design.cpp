class TrieNode {
public:
    // Initialize your data structure here.
    char val;
    vector<TrieNode*> next;
    TrieNode(char c) {
        val = c;
    }
    TrieNode() {
        val='/';
    }
};

class WordDictionary {
public:
    WordDictionary() {
        root = new TrieNode();
    }
    // Adds a word into the data structure.
    void addWord(string word) {
        string s = word+string("#");
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
    }
    
    bool DFS(string word, TrieNode* root){
        if(word.size()==0)
            return true;
        if(word[0]=='.'){
            for(int i =0; i<(root->next).size(); i++){
                if(DFS(word.substr(1),(root->next)[i]))
                    return true;
            }
        }
        else{
            for(int j=0; j<(root->next).size();j++){
                if((root->next)[j]->val==word[0]){
                    return DFS(word.substr(1),(root->next)[j]);
                }
            }
        }
        return false;
        
    }
    // Returns if the word is in the data structure. A word could
    // contain the dot character '.' to represent any one letter.
    bool search(string word) {
        word = word+string("#");
        return DFS(word,root);
    }
private:
    TrieNode* root;
};

// Your WordDictionary object will be instantiated and called as such:
// WordDictionary wordDictionary;
// wordDictionary.addWord("word");
// wordDictionary.search("pattern");
