/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
 
 // quick sort
class Solution1 {
public:
    ListNode* sortList(ListNode* head) {
        
    }
};

// merge sort
class Solution2 {
public:
    ListNode* merge(ListNode* l1, ListNode* l2){
     if(l1==NULL)
      return l2;
     if(l2 == NULL)
      return l1;
     ListNode* head = new ListNode(0);
     ListNode* temp = head;
     while(l1!=NULL && l2!=NULL){
      if(l1->val>l2->val){
       temp->next = l2;
       temp = temp->next;
       l2 = l2->next;
       temp->next = NULL;
     }
     else{
       temp->next = l1;
       temp = temp->next;
       l1 = l1->next;
       temp->next = NULL;
     }
    }
    if(l1==NULL)
     temp->next = l2;
    else temp->next=l1;
    return head->next;
    }
    ListNode* sortList(ListNode* head) {
        return mergeSort(head);
    }
    ListNode* mergeSort(ListNode* head){
      if(head==NULL || head->next==NULL)
       return head;
      ListNode * slow=head,*fast = head->next;
      while(fast!=NULL){
        fast = fast->next;
        if(fast==NULL)
            break;
        fast = fast->next;
        slow= slow->next;
      }
      fast = slow->next;
      slow->next = NULL;
      ListNode* l1 = mergeSort(head);
      ListNode* l2 = mergeSort(fast);
      return merge(l1,l2);
      }
};

//insert sort
class Solution3 {
public:
    ListNode* sortList(ListNode* head) {
        
    }
};

//radix sort
class Solution4 {
public:
    ListNode* sortList(ListNode* head) {
        
    }
};
