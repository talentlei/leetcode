/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
 
 /**
  * runtime : 12ms
  * error : 没有考虑else中pre与temp相等的情况！！ 记住 ！
  */
class Solution {
public:
    ListNode* partition(ListNode* head, int x) {
        ListNode thead(0);
        thead.next = head;
        ListNode* temp = &thead,*pre =&thead;
        while(temp->next!=nullptr){
            if(temp->next->val>=x)
                temp = temp->next;
            else{
                ListNode* t = temp->next;
                temp->next =temp->next->next;
                t->next = pre->next;
                pre->next = t;
                pre = t;
            }
        }
        return thead.next;
    }

/**
 *  another simple code!  great!
 *  runtime : 8ms
 *  
 * 
 */ 
class Solution1 {
public:
    ListNode* partition(ListNode* head, int x) {
        ListNode h1(0),h2(0);
        ListNode* l1 = &h1,*l2 =&h2;
        while(head!=nullptr){
            if(head->val>=x)   l2=l2->next=head;
            else   l1=l1->next=head;
            head=head->next;
        }
        l2->next = NULL;
        l1->next = h2.next;
        return h1.next;
    }
};
