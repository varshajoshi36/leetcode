'''
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    number = 0
    count = 0
    def inorderKTh(self, root):
        if root is not None:
            self.inorderKTh(root.left)
            self.count -= 1
            if self.count == 0:
                self.number = root.val
    
            self.inorderKTh(root.right)

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.count = k
        self.inorderKTh(root)
        return self.number
