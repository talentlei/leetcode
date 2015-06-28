/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
 /*
    runtime: 12ms
    error: 0
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* temp = head,*t;
        if(head==nullptr) return head;
        while(temp->next!=nullptr){
            if(temp->val==temp->next->val){
                t= temp->next;
                temp->next = temp->next->next;
                delete t;
            }else temp = temp->next;
        }return head;
    }
};
/*
    runtime:8ms
    error:0
*/
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        if(head==nullptr||head->next==nullptr)  return head;
        ListNode thead(0);
        ListNode *temp = &thead;
        int cnt = 1;
        while(head->next!=nullptr){
            if(head->val == head->next->val){
                cnt++; head = head->next;
            }
            else if(cnt==1){
                temp->next = head;
                temp = head;
                head = head->next;
            }else{
                cnt = 1;
                head=head->next;
            }
        }
        if(cnt==1){
            temp->next = head;
            temp = head;
        }
        temp->next = nullptr;
        return thead.next;
    }
};
