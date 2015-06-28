/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
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
    void reorderList(ListNode* head) {
        if(head==nullptr || head->next==nullptr) return head;
        int size =0;
        ListNode * temp = head;
        while(temp!=nullptr){
            size++; temp=temp->next;
        }
        int m = size-size/2;
        int i=0;
        temp = head;
        while(i<m-1){
            i++; temp= temp->next;
        }
        ListNode* beg = temp->next;
        temp->next = nullptr;
        ListNode * newbeg = reverseList(beg);
        i=0;
        beg = head;
        while(i<size/2){
            i++;
            temp = newbeg;
            newbeg = newbeg->next;
            temp->next = beg->next;
            beg->next =temp;
            beg = beg->next->next;
        }
        return head;
    }
};
