#include "tree.h"


int sumAtDepth(node* root, int depth){
	if(root == NULL || depth < 1)
		return -1;
	lnode* parent_stack = NULL;
	int level = 1;
	lnode* children_stack = NULL;
	push(&parent_stack, root);
	while(level < depth){
		while(!isEmpty(parent_stack)){
			node* parent = pop(&parent_stack);
			if(parent -> left)
				push(&children_stack, parent -> left);
			if(parent -> right)
				push(&children_stack, parent -> right);
		}
		while(!isEmpty(children_stack))
			push(&parent_stack, pop(&children_stack));
		level += 1;
	}

	int sum = 0;
	while(!isEmpty(parent_stack))
		sum += pop(&parent_stack) -> data;

	return sum;
}
