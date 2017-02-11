#include <stdio.h>
#include "tree.h"

node* newTreeNode(int data){
	node* new_node = (node *)malloc(sizeof(node));
	new_node -> data = data;
	new_node -> right = NULL;
	new_node -> left = NULL;
	return new_node;
}

void insert(node ** tree, int val){
        if(!(*tree)){
                node *temp = newTreeNode(val);
                *tree = temp;
                return;
        }

        if(val <= (*tree) -> data)
                insert(&((*tree) -> left), val);
        else
                insert(&((*tree) -> right), val);
}

void deleteTree(node * tree){
        if(tree){
                deleteTree(tree -> left);
                deleteTree(tree -> right);
                printf("Deleting node %d\n",tree -> data);
                free(tree);
        }
}

node* search(node ** tree, int val) {
        if(!(*tree))
                return NULL;
        if(val == (*tree) -> data)
                return *tree;
        else if(val < (*tree) -> data)
                search(&((*tree) -> left), val);
        else if(val > (*tree)->data)
                search(&((*tree) -> right), val);

}


