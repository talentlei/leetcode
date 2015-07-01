/**
 * Definition for singly-linked list with a random pointer.
 * struct RandomListNode {
 *     int label;
 *     RandomListNode *next, *random;
 *     RandomListNode(int x) : label(x), next(NULL), random(NULL) {}
 * };
 */
class Solution {
public:
    RandomListNode *copyRandomList(RandomListNode *head) {
        if(head==NULL) return NULL;
        RandomListNode* temp=head;
        while(temp!=NULL){
            RandomListNode *t = new RandomListNode(temp->label);
            t->next = temp->next;
            temp->next=t;
            temp = temp->next->next;
        }
        RandomListNode thead(0);
        temp = &thead;
        RandomListNode* cur1;
        for(cur1=head; cur1; cur1=cur1->next->next) {
      cur1->next->random = cur1->random? cur1->random->next:NULL;
    }
    for(cur1=head; cur1; cur1=cur1->next) {
      temp = temp->next = cur1->next;
      cur1->next = temp->next;
    }
         temp->next = NULL;
        return thead.next;
    }
};
