#include <stdio.h>
#include "tree.h"

int main(){
        node *root;

        root = NULL;

        insert(&root, 1);
        insert(&root, 4);
        insert(&root, 15);
        insert(&root, 6);
        insert(&root, 12);
        insert(&root, 17);
        insert(&root, 2);

        printf("Preorder:\n");
        preorder(root);
        
	printf("\nPostoredr:\n");
        postorder(root);
        
	printf("\nInorder\n");
        inorder(root);
        
	printf("\nIterative inorder:\n");
	itInorder(root);
        
	printf("\nPath to 17:\n");
        //node * rnode = search(&root, 15);
        node * rnode = printPath(&root, 17);
        printf("%d\n", rnode->data);
        
	deleteTree(root);
        return 0;
}
