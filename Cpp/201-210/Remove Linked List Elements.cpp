/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* removeElements(ListNode* head, int val) {
        if(head==NULL)
            return head;
        ListNode thead(0);
        thead.next = head;
        ListNode* cur = &thead;
        while(cur->next!=NULL){
            if(cur->next->val==val){
                cur->next = cur->next->next;
                continue;
            }
            cur = cur->next;
        }
        return thead.next;
    }
};
