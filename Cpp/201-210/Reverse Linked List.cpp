/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
 
 /*
    runtime :12ms
    error:0
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

/*
    runtime: 8ms
    error:0
*/
class Solution2 {
public:
    ListNode* reverseList(ListNode* head) {
        ListNode* thead = new ListNode(0);
        ListNode* temp;
        while(head!=NULL){
            temp = head->next;
            head->next = thead->next;
            thead->next = head;
            head = temp;
        }
        return thead->next;
    }
    
};
