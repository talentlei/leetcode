/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
 /*
  runtime :4ms
  error: 1
  time complexity : o(n);
 
 */
class Solution {
public:
    ListNode* swapPairs(ListNode* head) {
        ListNode* thead = new ListNode(0);
        ListNode* temp = thead;
        while(head!=NULL && head->next!=NULL){
          ListNode* t = head->next->next;
          head->next->next = head;
          temp->next = head->next;
          head->next = NULL;
          temp = temp->next->next;
          head = t;
        }
        return thead->next;
    }
};
