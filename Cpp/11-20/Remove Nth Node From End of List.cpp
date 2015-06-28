/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
 
 /*
    runtime: 4ms
    error:  0
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode thead(0);
        thead.next = head;
        ListNode* first = &thead,*second = &thead;
        int i=0;
        while(i<n){
            i++; 
            first = first->next;
        }
        while(first->next!=nullptr){
            first=first->next; 
            second = second->next;
        }
        first = second->next;
        second->next = second->next->next;
        delete first;
        return thead.next;
    }
};
