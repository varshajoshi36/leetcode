#include <stdbool.h>

struct bnode{
        int data;
        struct bnode* left;
        struct bnode* right;
};

struct lnode{
        int data;
	struct bnode* tnode;
        struct lnode* next;
};

typedef struct bnode node;
typedef struct lnode lnode;

node* newTreeNode(int);
void insert(node **, int);
void preorder(node *);
void postorder(node *);
void inorder(node *);
node* printPath(node **, int);
node* search(node **, int);
void deleteTree(node *);
bool isEmpty(lnode*);
node* pop(lnode**);
void push(lnode**, node *);
void iteInorder(node *);
