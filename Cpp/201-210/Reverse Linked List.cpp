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
    ListNode* reverseList(ListNode* head) {
        if(head==NULL || head->next==NULL)
            return head;
        ListNode *cur,*temp;
        cur = head;
        while(cur->next!=NULL){
            temp = cur->next;
            cur->next = cur->next->next;
            temp->next = head;
            head = temp;
        }
        return head;
    }
};
