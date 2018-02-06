"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
Example 1:
    2
   / \
  1   3
Binary tree [2,1,3], return true.
Example 2:
    1
   / \
  2   3
Binary tree [1,2,3], return false.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):    
    def inorderTraversal(self, root, bst_array):
        if root:
            self.inorderTraversal(root.left, bst_array)
            bst_array.append(root.val)
            self.inorderTraversal(root.right, bst_array)
            
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        bst_array = []
        self.inorderTraversal(root, bst_array)
        for i in range(len(bst_array) - 1):
            if bst_array[i] >= bst_array[i + 1]:
                return False
        return True
