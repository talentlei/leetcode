/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 
 /**
  * 
  * runtime: 28ms
  * error: 0
  * 
  */ 
class BSTIterator {
public:
    BSTIterator(TreeNode *root) {
        cur = root;    
    }

    /** @return whether we have a next smallest number */
    bool hasNext() {
        return (!myStack.empty()|| cur!=NULL);
    }

    /** @return the next smallest number */
    int next() {
        while(cur){
            myStack.push(cur);
            cur = cur->left;
        }
        cur=myStack.top();
        myStack.pop();
        int val = cur->val;
        cur = cur->right;
        return val;
    }
private:
    stack<TreeNode*> myStack;
    TreeNode* cur;
    
};

/**
 * Your BSTIterator will be called like this:
 * BSTIterator i = BSTIterator(root);
 * while (i.hasNext()) cout << i.next();
 */
