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
        
	int closest1 = closestMatch(root, 18);
	printf("\nClosest: %d\n", closest1);
	lnode* stack = NULL;
	int min_sum = minPath(root);
	int sum = 0;
	printf("Min sum Path: %d\n",min_sum);
	printMinPath(root, stack, min_sum, &sum);
	deleteTree(root);
 
	//tree 2:
	printf("*** tree2");
	int num[13] = {22,20,14,21,13,19,7,5,11,17,16,18,23};
	node* root2 = NULL;
	int i;
	for(i = 0; i < 13; i++)
		insert(&root2, num[i]);
	printf("\nPreorder\n");
        preorder(root2);
        
	printf("\nIterative preorder:\n");
	itPreorder(root2);
	
	node* tnode = search(&root2, 14);
	node* succ = inorderSuccessor(root2, tnode);
	printf("Inorder successor of %d is %d\n", tnode -> data, succ -> data);
	printf("\nInorder after deleting\n");
        inorder(root2);
	int kthSmallest = kThSmallest(root2, 3);
	printf("3rd smallest node: %d", kthSmallest);
	printf("\npostorder traversal with one stack: \n");
	itPostorder(root2);
	printf("\n");
	lnode* stack1 = NULL;
        int min_sum1 = minPath(root);
        printf("MinSum: %d\n", min_sum1);
	int sum1 = 0;
        printf("Min sum Path2: \n");          
        printMinPath(root2, stack1, min_sum1, &sum1);	
	int closest = closestMatch(root2, 12);
	printf("\nClosest: %d\n", closest);
	printf("\n");
	
	//tree 3
	int num2[9] = {5,3,7,2,4,6,8,1,10};
	node* root3 = NULL;
	for(i = 0; i < 9; i++)
	                insert(&root3, num2[i]);
	int sum3 = sumAtDepth(root3, 0);
	printf("tree3 sum at node 3: %d\n", sum3);
	return 0;
}
