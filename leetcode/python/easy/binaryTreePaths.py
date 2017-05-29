'''
Given a binary tree, return all root-to-leaf paths.

For example, given the following binary tree:

   1
 /   \
2     3
 \
  5
All root-to-leaf paths are:

["1->2->5", "1->3"]
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def binaryTreePaths(self, root):
    """
    :type root: TreeNode
    :rtype: List[str]
    """
    if root == None:
        return []

    if root.left == None and root.right == None:
        return [str(root.val)]
    
    left = binaryTreePaths(root.left)
    right = binaryTreePaths(root.right)

    total_paths = left + right

    total_paths = [str(root.val) + "->" + path for path in total_paths]

    return total_paths
