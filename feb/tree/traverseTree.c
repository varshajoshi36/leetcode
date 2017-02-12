#include <stdio.h>
#include "tree.h"

void preorder(node * tree){
        if(tree){
                printf("%d\t", tree -> data);
                preorder(tree -> left);
                preorder(tree -> right);
        }
}

void postorder(node * tree){
        if(tree){
                postorder(tree -> left);
                postorder(tree -> right);
                printf("%d\t", tree -> data);
        }
}

void inorder(node * tree){
        if(tree){
                inorder(tree -> left);
                printf("%d\t", tree -> data);
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

void itPreorder(node *tree){
	node *current = tree;
        lnode *stack =  NULL;
        bool done = 0;

        while(!done){
                if(current != NULL){
                        printf("%d\t", current -> data);
                        push(&stack, current);
                        current = current -> left;
                }else{
                        if(!isEmpty(stack)){
                                node* tnode = pop(&stack);
                                current = tnode -> right;
                        }else{
                                done = 1;
                        }
                }
        }
}


void itPostorder(node *tree){
	node* current = tree;
	lnode* stack1 = NULL;
	lnode* stack2 = NULL;
	
	push(&stack1, tree);
	
	while(!isEmpty(stack1)){
		current = pop(&stack1);
		
		if(current -> left != NULL)
			push(&stack1, current -> left);
		if(current -> right != NULL)
			push(&stack1, current -> right);

		push(&stack2, current);
	}

	while(!isEmpty(stack2)){
		node* tmp = pop(&stack2);
		printf("%d\t", tmp -> data);
	}
}

node* inorderSuccessor(node* root, node* tnode){
	node* succ = NULL;
	if(tnode -> right != NULL){
		succ = getMinNode(tnode -> right);
		return succ;
	}
	node* current = root;
	while(current != NULL){
		if(tnode -> data < current -> data){
			succ = current;
			current = current -> left;
		}else if(tnode -> data > current -> data){
			current = current -> right;
		} else
			break;
	}
	return succ;
}


int kThSmallest(node *tree, int k){
	node *current = tree;
	lnode *stack = 	NULL;
	bool done = 0;
	lnode* sortedList = NULL;
	int size = 0;
	while(!done){
		if(current != NULL){
			push(&stack, current);
			current = current -> left;
		}else{
			if(!isEmpty(stack)){
				node* tnode = pop(&stack);
				push(&sortedList, tnode);
				size++;
				current = tnode -> right;
			}else{
				done = 1;
			}
		}
	}
	int i = size;
	node* kThSmallest = NULL;
	while(i >= k){
		kThSmallest = pop(&sortedList);
		i--;
	}
	return kThSmallest -> data;
}
