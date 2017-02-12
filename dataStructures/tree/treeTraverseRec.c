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
