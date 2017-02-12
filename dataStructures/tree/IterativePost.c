#include "tree.h"

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

void ItPostorderOneStack(node* root)
{
    // Check for empty tree
    if (root == NULL)
        return;

    lnode* stack = NULL;
    do
    {
        // Move to leftmost node
        while (root)
        {
            // Push root's right child and then root to stack.
            if (root->right)
                push(&stack, root->right);
            push(&stack, root);

            // Set root as root's left child  
            root = root->left;
        }

        // Pop an item from stack and set it as root    
        root = pop(&stack);

        // If the popped item has a right child and the right child is not
        // processed yet, then make sure right child is processed before root
        if (root->right && peek(stack) == root->right)
        {
            pop(&stack);  // remove right child from stack
            push(&stack, root);  // push root back to stack
            root = root->right; // change root so that the right 
                                // child is processed next
        }
        else  // Else print root's data and set root as NULL
        {
            printf("%d ", root->data);
            root = NULL;
        }
	} while (!isEmpty(stack));
}

