/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
 
 /*
    runtime: 4ms
    error: 0
 */
class Solution {
public:
    vector<vector<int>> zigzagLevelOrder(TreeNode* root) {
        vector<vector<int> > res;
        if(root==NULL) return res;
        stack<TreeNode*> myStack;
        stack<TreeNode*> temp;
        int isleft=1;
        myStack.push(root);
        while(!myStack.empty()){
            vector<int> one;
            while(!myStack.empty()){
                TreeNode* node = myStack.top();
                myStack.pop();
                one.push_back(node->val);
                if(isleft==1){
                    if(node->left!=NULL)  temp.push(node->left);
                    if(node->right!=NULL)  temp.push(node->right);
                }else{
                    if(node->right!=NULL) temp.push(node->right);
                    if(node->left!=NULL)  temp.push(node->left);
                }
            }
            isleft*=-1;
            myStack.swap(temp);
            res.push_back(one);
        }
        return res;
    }
};
