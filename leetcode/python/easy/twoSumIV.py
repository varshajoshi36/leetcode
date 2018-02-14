"""
Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True
Example 2:
Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 28

Output: False
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getDiffs(self, root, diff_array, target):
        if root:
            diff = target -root.val
            if root.val in diff_array:
                return True
            if diff not in diff_array:
                diff_array.append(diff)
            return self.getDiffs(root.left, diff_array, target) or self.getDiffs(root.right, diff_array, target)
        else:
            return False
        
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        diff_array = []
        return self.getDiffs(root, diff_array, k)
        
        
