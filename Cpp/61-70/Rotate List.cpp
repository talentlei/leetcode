/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
 /*
  runtime:12ms
  error : 1 divide zero error when len =0;
  
 */
class Solution {
public:
ListNode* rotateRight(ListNode* head, int k) {
      int len=0;
      ListNode* temp = head;
      while(temp!=NULL)
      { len++; temp=temp->next;}
      if(k==0||len==0) return head;
      k = k%len;
      int cnt=0;
      ListNode* pre =head, *aft = head;
      while(cnt<k)
      {aft=aft->next; cnt++;}
      while(aft->next!=NULL)
      {  aft=aft->next; pre=pre->next;    }
      aft->next = head;
      head = pre->next;
      pre->next = NULL;
      return head;
    }
};
