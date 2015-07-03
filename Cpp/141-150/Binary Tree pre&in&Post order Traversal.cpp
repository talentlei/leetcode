/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    /**
     *  runtime:0ms
     *  error: 0
     * 
     */ 
    vector<int> preorderTraversal(TreeNode* root) {
      vector<int> res;
      stack<TreeNode*> myStack;
      TreeNode* p = root;
      while(!myStack.empty()||p){
        while(p){
            myStack.push(p);
            res.push_back(p->val);
            p=p->left;
      }
      p = myStack.top();
      myStack.pop();
      p = p->right;
    }
    return res;
    }
    /**
     * runtime: 4ms
     * error: 2
     * 当将元素输出时，1更新pre，2同时pop该元素   
     * 
     */ 
    vector<int> postorderTraversal(TreeNode* root) {
        vector<int > res;
        if(root==NULL) return res;
        stack<TreeNode*> myStack;
        TreeNode* pre=0,*p;
        myStack.push(root);
        while(!myStack.empty()){
            p = myStack.top();
            if(p->left==NULL&&p->right==NULL || (pre!=NULL&&(pre==p->left||pre==p->right))){
                res.push_back(p->val);
                myStack.pop();
                pre = p;
            }
            else{
                if(p->right) myStack.push(p->right);
                if(p->left) myStack.push(p->left);
            }
        }
        return res;
    }
    /**
     *  runtime:0ms
     *  error: 0
     * 
     */ 
    vector<int> inorderTraversal(TreeNode* root) {
      vector<int> res;
      stack<TreeNode*> myStack;
      TreeNode* p = root;
      while(!myStack.empty()||p){
        while(p){
            myStack.push(p);
            p=p->left;
      }
      p = myStack.top();
      res.push_back(p->val);
      myStack.pop();
      p = p->right;
    }
    return res;
    }
};
