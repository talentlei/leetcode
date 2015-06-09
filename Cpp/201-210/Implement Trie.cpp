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

class Trie {
public:
    Trie() {
        root = new TrieNode();
    }

    // Inserts a word into the trie.
    void insert(string s) {
        s = s+string("#");
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
                    // TrieNode node(s[i]);
                    // cur->next.push_back(&node);
                    // cur = &node;
                    TrieNode* node = new TrieNode(s[i]);
                    cur->next.push_back(node);
                    cur = node;
                    i++;
                }
            }
        }
    }

    // Returns if the word is in the trie.
    bool search(string key) {
        string t = key+string("#");
        TrieNode * cur= root;
        for(int i=0; i<t.size(); i++){
            bool isFound = false;
            for(int j=0; j< (cur->next).size(); j++){
                if((cur->next)[j]->val==t[i]){
                    isFound = true;
                    cur = (cur->next)[j];
                    break;
                }
            }
            if(!isFound)
                return false;
        }
        return true;
    }

    // Returns if there is any word in the trie
    // that starts with the given prefix.
    bool startsWith(string prefix) {
        string t = prefix;
        TrieNode * cur= root;
        for(int i=0; i<t.size(); i++){
            bool isFound = false;
            for(int j=0; j< (cur->next).size(); j++){
                if((cur->next)[j]->val==t[i]){
                    isFound = true;
                    cur = (cur->next)[j];
                    break;
                }
            }
            if(!isFound)
                return false;
        }
        return true;
    }

private:
    TrieNode* root;
};

// Your Trie object will be instantiated and called as such:
// Trie trie;
// trie.insert("somestring");
// trie.search("key");
