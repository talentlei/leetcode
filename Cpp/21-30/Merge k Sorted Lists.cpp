/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
 /*
    runtime: 424ms  slow
    error:0
 */
class Solution {
public:
    ListNode* mergeKLists(vector<ListNode*>& lists) {
        if(lists.size()==0) return NULL;
        return mergeK(lists,0,lists.size()-1);
    }
    ListNode* mergeK(vector<ListNode*>& lists, int beg, int end){
        if(beg>end)     return NULL;
        if(beg==end)    return lists[beg];
        int mid=beg+(end-beg)/2;
        ListNode* l1 = mergeK(lists,beg,mid);
        ListNode* l2 = mergeK(lists,mid+1,end);
        return mergeTwoLists(l1,l2);
    }
    ListNode* mergeTwoLists(ListNode* l1, ListNode* l2) {
        if(l1==NULL) return l2;
        if(l2==NULL) return l1;
        ListNode head(0),*temp=&head;
        while(l1!=NULL&&l2!=NULL){
            if(l1->val<l2->val){
                temp= temp->next = l1;
                l1 = l1->next;
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
