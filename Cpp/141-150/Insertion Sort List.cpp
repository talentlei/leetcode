/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
 
 /*
    runtime： 84ms
    error : 0
    time complexity :O(n^2)
 
 */
class Solution {
public:
    ListNode* insertionSortList(ListNode* head) {
      if(head==NULL||head->next==NULL)
        return head;
      ListNode* thead = new ListNode(0);
      ListNode* cur = head,*temp;
      while(cur!=NULL){
        temp = thead;
        while(temp->next!=NULL&&cur->val>=temp->next->val)
          temp = temp->next;
        ListNode* t = cur->next;
        cur->next = temp->next;
        temp->next = cur;
        cur = t;
      }
      return thead->next;
    }
};
