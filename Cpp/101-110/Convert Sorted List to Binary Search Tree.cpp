/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
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
    runtime:28ms
    error:0
 */
class Solution {
public:
    TreeNode* sortedListToBST(ListNode* head) {
        int len=0;
        ListNode* temp =head;
        while(temp){
            len++; temp =temp->next;
        }
        return sortedList2BST(head,len);
    }
    TreeNode* sortedList2BST(ListNode*head,int len){
        if(len==0) return NULL;
        TreeNode* node;
        if(len==1) return new TreeNode(head->val);
        int mid = len/2,i=0;
        ListNode* t =head;
        while(i<mid-1){
            t = t->next;
            i++;
        }
        node = new TreeNode(t->next->val);
        node->right = sortedList2BST(t->next->next,len-mid-1);
        t->next = NULL;
        node->left = sortedList2BST(head,mid);
        return node;
    }
};
