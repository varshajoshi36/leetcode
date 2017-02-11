#include <stdio.h>
#include <stdbool.h>
#include "tree.h"

void push(lnode** top_ref, node *tnode){
	lnode* new_node = (lnode *)malloc(sizeof(lnode));
	new_node -> tnode = tnode;
	new_node -> next = *top_ref;
	(*top_ref) = new_node;	
}

node* pop(lnode** top_ref){
	lnode* top_node = *top_ref;
	if(isEmpty(*top_ref)){
		printf("Stack Underflow \n");
		getchar();
		exit(0);
	}
		
	node* res = top_node -> tnode;
	*top_ref = (top_node) -> next;
	return res;
}

bool isEmpty(lnode *top){
   return (top == NULL)? 1 : 0;
}   
