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
        
	printf("\nIterative preorder:\n");
	itPreorder(root);

	printf("\nPostoredr:\n");
        postorder(root);
        
	printf("\nIterative postorder:\n");
	itPostorder(root);

	printf("\nInorder\n");
        inorder(root);
        
	printf("\nIterative inorder:\n");
	itInorder(root);
        
	printf("\nPath to 17:\n");
        //node * rnode = search(&root, 15);
        node * rnode = printPath(&root, 17);
        printf("%d\n", rnode->data);
        
	deleteTree(root);
        
	//tree 2:
	int num[12] = {22,20,14,21,13,19,7,5,11,17,16,18};
	node* root2 = NULL;
	int i;
	for(i = 0; i<12; i++)
		insert(&root2, num[i]);
	node* tnode = search(&root2, 14);
	node* succ = inorderSuccessor(root2, tnode);
	printf("Inorder successor of %d is %d\n", tnode -> data, succ -> data);
	printf("\nInorder after deleting\n");
        inorder(root2);
	int kthSmallest = kThSmallest(root2, 3);
	printf("3rd smallest node: %d", kthSmallest);
	printf("\n");
	return 0;
}
