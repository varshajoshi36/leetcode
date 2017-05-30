'''
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if root == None:
                return []

        if root.left == None and root.right == None and sum - root.val == 0:
                return [[root.val]]

        left_path = self.hasPathSum(root.left, sum - root.val)
        right_path = self.hasPathSum(root.right, sum - root.val)

        total_paths = left_path + right_path

        if len(total_paths) > 0:
            total_paths = [[root.val] + path for path in total_paths]

        return total_paths

