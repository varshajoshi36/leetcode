"""
Given two binary trees, write a function to check if they are equal or not.

Two binary trees are considered equal if they are structurally identical and the nodes have the same value.
"""

def isSameTree(p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    if p == None and q == None:
        return True
    elif p.val == q.val:
        isRightSame = isSameTree(p.right, q.right)
        isLeftSame = isSameTree(p.left, q.left)
        if isRightSame and isLeftSame:
            return True
    else:
        return False
