#include <stdio.h>
#include "tree.h"

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
	int kThSmallest = -1;
	while(!done){
		if(current != NULL){
			push(&stack, current);
			current = current -> left;
		}else{
			if(!isEmpty(stack)){
				node* tnode = pop(&stack);
				push(&sortedList, tnode);
				size++;
				if (size == k)
					return tnode -> data;
				current = tnode -> right;
			}else{
				done = 1;
			}
		}
	}
	return kThSmallest;
}

int minPath(node* root){
	if(root == NULL)
		return 0;

	int sum = root -> data;

	int left_sum = minPath(root -> left);
	int right_sum = minPath(root -> right);

	if(left_sum < right_sum)
		sum += left_sum;
	else
		sum += right_sum;

	return sum;
}

void printMinPath(node* root, lnode* stack, int minsum, int* sum){
	if(root != NULL){
		push(&stack, root);
		*sum += root -> data;
		if(*sum == minsum){
			while(!isEmpty(stack)){
				node* pnode = pop(&stack);
				if(pnode)
					printf("-> %d", pnode -> data);
			}
			printf("\n");
			return;
		}
		printMinPath(root -> left, stack, minsum, sum);
		printMinPath(root -> right, stack, minsum, sum);
		if(!isEmpty(stack))
			pop(&stack);
		*sum -= root -> data;
	}else{
		return;
	}

}
