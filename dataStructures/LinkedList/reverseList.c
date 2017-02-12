#include <stdio.h>
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseList(struct ListNode* head) {
    
    if(head == NULL) {
        return NULL;
    }
    
    if(head->next == NULL) {
        return head;
    }
    
    struct ListNode* follow = NULL;
    struct ListNode* back = head;
    struct ListNode* front = head->next;
    
    while(back != NULL) {
        front = back->next;
        back->next = follow;
        follow = back;
        back = front;
    }
    
    return follow;
}
