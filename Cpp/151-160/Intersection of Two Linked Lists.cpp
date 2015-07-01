/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
 /*
    runtime: 52ms
    errot:0
 */
class Solution {
public:
    ListNode *getIntersectionNode(ListNode *headA, ListNode *headB) {
        if(headA==NULLL || headB==NULL) return NULL;
        int lenA = 1, lenB=1; 
        ListNode* tA = headA,*tB = headB;
        while(tA->next!=NULL){
            lenA++; tA=tA->next;
        }
        while(tB->next!=NULL){
            lenB++; tB=tB->next;
        }
        if(tA!=tB) return NULL;
        int i=0; 
        if(lenA>lenB){
            while(i<lenA-lenB)
            { headA=headA->next; i++;}
        }else{
            while(i<lenB-lenA)
            { headB=headB->next; i++; }
        }
        while(headA!=headB){
            headA=headA->next;
            headB=headB->next;
        }
        return headA;
    }
};
