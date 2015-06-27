/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
 
 /*
    runtime: 24ms
    error:1  
        if(head!=NULL)   //forget this condition
            temp->next = beg;
      
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
    ListNode* reverseKGroup(ListNode* head, int k) {
        if(k<2) return head;
        ListNode* thead= new ListNode(0);
        ListNode* temp = thead;
        ListNode* beg;
        while(head!=NULL){
          int i=0; 
          beg = head;
          while(i<k-1&&head->next!=NULL){
            i++;
            head =head->next;
          }
          if(i!=k-1) break;
          ListNode* t = head->next;
          head->next = NULL;
          temp->next = reverseList(beg);
          temp = beg;
          head =t;
        }
        if(head!=NULL)
            temp->next = beg;
        return thead->next;
    }
};
