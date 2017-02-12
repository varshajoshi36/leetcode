#include <stdio.h>
#include <stdlib.h>

struct lnode{
	int data;
	struct lnode* next;
};

typedef struct lnode lnode;

lnode* removeNodes(lnode*, int);
void printList(lnode*);
void addNode(lnode**, int);

int main(){
	int nums[11] = {1,1,1,2,2,1,3,2,4,2,1};
	int i;
	lnode* head = NULL;
	for(i = 0; i < 11; i++)
		addNode(&head, nums[i]);

	printList(head);
	lnode* newHead = removeNodes(head, 1);
	printList(newHead);
	return 0;
}

lnode* removeNodes(lnode* head, int val){
	lnode* tmp = NULL;
	while(head != NULL && head -> data == val){
		tmp = head;
		head = head -> next;
		free(tmp);
	}
	if(head == NULL)
		return NULL;

	lnode* current = head;
	while(current != NULL && current -> next != NULL){
		if(current -> next -> data == val){
			tmp = current -> next;
			current -> next =  current -> next -> next;
			free(tmp);
		}else{
			current = current -> next;
		}
	}
	return head;
}



void printList(lnode* head){
	lnode* current = head;
	while(current != NULL){
		printf("%d", current -> data);
		current = current -> next;
	}
	printf("\n");
}

void addNode(lnode** head, int val){
	if(*head == NULL){
		lnode* new_node = (lnode *)malloc(sizeof(lnode));
		new_node -> next = NULL;
		new_node -> data = val;

		*head = new_node;
		return;
	}else
		addNode(&((*head) -> next), val);

}
