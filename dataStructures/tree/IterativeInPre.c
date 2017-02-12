#include "tree.h"

void itInorder(node *tree){
        node *current = tree;
        lnode *stack =  NULL;
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
