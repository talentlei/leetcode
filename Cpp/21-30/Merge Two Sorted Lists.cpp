/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
 
 /*
    runtime:8ms
    error:0
 */
class Solution {
public:
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if(l1==NULL) return l2;
        if(l2==NULL) return l1;
        ListNode head(0),*temp=&head;
        while(l1!=NULL&&l2!=NULL){
            if(l1->val<l2->val){
                temp= temp->next = l1;
                l1 = l1.next;
                temp->next=NULL;
            }else{
                temp=temp->next=l2;
                l2=l2->next;
                temp->next=NULL;
            }
        }if(l1==NULL) temp->next = l2;
        else temp->next = l1;
        return head.next;
    }
};
