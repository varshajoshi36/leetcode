"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
"""

def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
            
        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        
        if root.left != None and root.right != None:
            return 1 + min(left, right)
        else:
            return 1 + max(left, right)
