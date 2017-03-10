'''
Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root.right is None and root.left is None:
            return root
        elif root.right is None:
            root.right = invertTree(root.left)
            root.left = None
            return root
        elif root.left is None:
            root.left = invertTree(root.right)
            root.right = None
            return root
        else:
            leftTree = root.left
            root.left = invertTree(root.right)
            root.right = invertTree(leftTree)
            return root
