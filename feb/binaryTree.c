#include <stdio.h>
#include<stdlib.h>

struct bnode{
	int data;
	struct bnode* left;
	struct bnode* right;
};

typedef struct bnode node;

void insert(node **, int);
void preorder(node *);
void postorder(node *);
void inorder(node *);
node* printPath(node **, int);
node* search(node **, int);
void deleteTree(node *);

int main(){
	node *root;
	node *tmp;

	root = NULL;

	insert(&root, 1);
	insert(&root, 4);
	insert(&root, 15);
	insert(&root, 6);
	insert(&root, 12);
	insert(&root, 17);
	insert(&root, 2);

	preorder(root);
	printf("\n");
	postorder(root);
	printf("\n");
	inorder(root);
	printf("\n");
	//node * rnode = search(&root, 15);
	node * rnode = printPath(&root, 17);
	printf("%d\n", rnode->data);
	deleteTree(root);
	return 0;
}

void insert(node ** tree, int val){
	if(!(*tree)){
		node *temp = (node *)malloc(sizeof(node));
		temp -> left = NULL;
		temp -> right = NULL;
		temp -> data = val;

		*tree = temp;
		return;
	}

	if(val <= (*tree) -> data)
		insert(&((*tree) -> left), val);
	else
		insert(&((*tree) -> right), val);
}

void preorder(node * tree){
	if(tree){
		printf("%d\t",tree -> data);
		preorder(tree -> left);
		preorder(tree -> right);
	}
}

void postorder(node * tree){
	if(tree){
		postorder(tree -> left);
		postorder(tree -> right);
		printf("%d\t",tree -> data);
	}
}

void inorder(node * tree){
	if(tree){
		inorder(tree -> left);
		printf("%d\t",tree -> data);
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


node* search(node ** tree, int val) {
	if(!(*tree)) {
		return NULL;
	}
	if(val == (*tree) -> data) {
		return *tree;
	} else if(val < (*tree) -> data) {
		search(&((*tree) -> left), val);
	} else if(val > (*tree)->data){
		search(&((*tree) -> right), val);
	}
}

void deleteTree(node * tree){
	if(tree){
		deleteTree(tree -> left);
		deleteTree(tree -> right);
		printf("Deleting node %d\n",tree -> data);
		free(tree);
	}	
}
