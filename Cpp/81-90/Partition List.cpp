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
    ListNode* partition(ListNode* head, int x) {
        ListNode thead(0);
        thead.next = head;
        ListNode* temp = &thead,*pre =&thead;
        while(temp->next!=nullptr){
            if(temp->next->val>=x)
                temp = temp->next;
            else{
                ListNode* t = temp->next;
                temp->next =t->next;
                t->next = pre->next;
                pre->next = t;
                pre = t;
            }
        }
        return thead.next;
    }
};
