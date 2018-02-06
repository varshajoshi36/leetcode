"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def checkLeftRight(self, l_root, r_root):
        if l_root == None or r_root == None:
            if l_root == None and r_root == None:
                return True
            else:
                return False
        elif l_root.val == r_root.val:
            is_left_mirror = self.checkLeftRight(l_root.left, r_root.right)
            is_right_mirror = self.checkLeftRight(l_root.right, r_root.left)
            return is_left_mirror and is_right_mirror
        else:
            return False
            
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        return self.checkLeftRight(root.left, root.right)
