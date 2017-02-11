#include <stdio.h>
#include "tree.h"

void preorder(node * tree){
        if(tree){
                printf("%d\t",tree -> data);
                preorder(tree -> left);
                preorder(tree -> right);
        }
}

void postorder(node * tree){
        if(tree){
                postorder(tree -> left);
                postorder(tree -> right);
                printf("%d\t",tree -> data);
        }
}

void inorder(node * tree){
        if(tree){
                inorder(tree -> left);
                printf("%d\t",tree -> data);
                inorder(tree -> right);
        }
}

node* printPath(node ** tree, int val){
        if (!(*tree))
                return NULL;
        else if(val == (*tree) -> data ){
                return *tree;
        }else if(((*tree) -> data) > val){
                node* prev = printPath((&(*tree) -> left), val);
                if (prev){
                        printf("%d\t<-", (prev) -> data);
                        return *tree;
                }
        }else{
                node* prev = printPath((&(*tree) -> right), val);
                if(prev){
                        printf("%d\t<-\t", (prev) -> data);
                        return *tree;
                }
        }
}

void itInorder(node *tree){
	node *current = tree;
	lnode *stack = 	NULL;
	bool done = 0;

	while(!done){
		if(current != NULL){
			push(&stack, current);
			current = current -> left;
		}else{
			if(!isEmpty(stack)){
				node* tnode = pop(&stack);
				printf("%d\t", tnode -> data);
				current = tnode -> right;
			}else{
				done = 1;
			}
		}
	}
}
