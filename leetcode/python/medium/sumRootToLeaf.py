"""
Given a binary tree containing digits from 0-9 only, each root-to-leaf path could represent a number.

An example is the root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

For example,

    1
   / \
  2   3
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.

Return the sum = 12 + 13 = 25.
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recSum(self, root, prev_sum):
        if root == None:
            return 0
        elif root.left == None and root.right == None:
            return prev_sum * 10 + root.val
        else:
            return self.recSum(root.left, prev_sum * 10 + root.val) + self.recSum(root.right, prev_sum * 10 + root.val)
    
    
    def sumNumbers(self, root):
        return self.recSum(root, 0)
    
    def getNumbers(self, root, upper_level_number, stack):
        if root != None:
            if root.left == None and root.right == None:
                stack.append(upper_level_number*10 + root.val)
            else:
                this_level_number = upper_level_number * 10 + root.val
                self.getNumbers(root.left, this_level_number, stack)
                self.getNumbers(root.right, this_level_number, stack)
    
    def sumNumbers1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        stack = []
        self.getNumbers(root, 0, stack)
        return sum(stack)
