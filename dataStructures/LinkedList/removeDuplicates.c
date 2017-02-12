/* Program to remove duplicates in an unsorted array */
 
#include<stdio.h>
#include<stdlib.h>
 
struct node{
 int data;
 struct node *next;
};
 
void removeDuplicates(struct node *start){
  struct node *ptr1, *ptr2, *dup;
  ptr1 = start;
 
  while(ptr1 != NULL && ptr1->next != NULL){
     ptr2 = ptr1;
 
     while(ptr2->next != NULL){
       if(ptr1->data == ptr2->next->data){
          dup = ptr2->next;
          ptr2->next = ptr2->next->next;
          free(dup);
       }
       else {
          ptr2 = ptr2->next;
       }
     }
     ptr1 = ptr1->next;
  }
}
 
void push(struct node** head_ref, int new_data);
 
void printList(struct node *node);
 
int main(){
  struct node *start = NULL;
 
  push(&start, 10);
  push(&start, 11);
  push(&start, 12);
  push(&start, 11);
  push(&start, 11);
  push(&start, 12);
  push(&start, 10);
 
  printf("\n Linked list before removing duplicates ");
  printList(start);
 
  removeDuplicates(start);
 
  printf("\n Linked list after removing duplicates ");
  printList(start);
  printf("\n");

  return 0; 
}
 
void push(struct node** head_ref, int new_data){
  struct node* new_node =
            (struct node*) malloc(sizeof(struct node));
 
  new_node->data  = new_data;
 
  new_node->next = (*head_ref);
 
  (*head_ref)    = new_node;
}
 
void printList(struct node *node){
  while(node != NULL){
    printf("%d ", node->data);
    node = node->next;
  }
}
