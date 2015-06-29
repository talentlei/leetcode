/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
 /**
  * runtime: 13ms
  * error:0
  */ 
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if(head==NULL) return false;
        ListNode* fast = head, *slow=head;
        while(fast!=NULL){
            fast=fast->next;
            if(fast==NULL)
                return false;
            fast = fast->next;
            slow = slow->next;
            if(fast==slow)
                return true;
        }
        return false;
    }
};

follow up:


/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
 
 /**
  * runtime: 15ms
  * error:1
  *  * 
  */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if(head==NULL) return false;
        ListNode* fast = head, *slow=head;
        while(fast!=NULL){
            fast=fast->next;
            if(fast==NULL)
                return false;
            fast = fast->next;
            slow = slow->next;
            if(fast==slow)
                return true;
        }
        return false;
    }
    ListNode *detectCycle(ListNode *head) {
        if(hasCycle(head)) return NULL;      
        ListNode* fast=head->next->next,*slow=head->next;  //attention
        while(fast!=slow){
            fast = fast->next->next;
            slow = slow->next;
        }
        slow=head;
        while(slow!=fast){
            fast=fast->next;
            slow = slow->next;
        }
        return slow;
    }
};
