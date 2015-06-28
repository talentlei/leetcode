/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
 
 /*
    runtime:4ms
    error: 2;   m==n and temp= thead;
 
 */
class Solution {
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
    ListNode* reverseBetween(ListNode* head, int m, int n) {
      if(m==n)
        return head;
      ListNode* thead = new ListNode(0);
      thead->next = head;
      ListNode* temp = thead;
      int i=0; 
      while(i<m-1)
      { i++; temp =temp->next;}
      head =temp->next; i++;
      ListNode* beg = head;
      while(i<n)
      { i++; head = head->next;}
      ListNode* t = head->next;
      head->next = NULL;
      temp->next = reverseList(beg);
      beg->next = t;
      return thead->next;
      
    }
};
