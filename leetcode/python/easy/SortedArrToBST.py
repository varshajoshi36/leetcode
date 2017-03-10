'''
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recSortedToBST(self, start, end, nums, root):
        if start < end:
            mid = (start + end)/2
            tempNode = root
            while tempNode != None:
                if nums[mid] > tempNode.val:
                    if tempNode.right is None:
                        tempNode.right = TreeNode(nums[mid])
                        tempNode = tempNode.right
                    tempNode = tempNode.right
                elif:
                    if tempNode.left is None:
                        tempNode.left = TreeNode(nums[mid])
                        tempNode = tempNode.left
                    tempNode = tempNode.left
            self.recSortedToBST(start, mid - 1, nums, root)
            self.recSortedToBST(mid + 1, end, nums, root)
    
            
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        length = len(nums)
        start = 0
        end = length -1
        mid = (start + end)/2
        root = TreeNode(nums[mid])
        if start < end:
            self.recSortedToBST(start, mid - 1, nums, root)
            self.recSortedToBST(mid + 1, end, nums, root)

        return root
