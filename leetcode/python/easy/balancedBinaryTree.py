"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.
"""
def isBalanced(root):
   
    def check(root):
        if root == None:
            return 0
        left = check(root.left)
        right = check(root.right)

        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        
        return 1 + max(left, right)

    return check(root) != -1


"""
Following solution tells if the tree as a whole is balanced. (Not sure if there is concept like that)
"""

def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        leaves = []
        parents = []
        parents.append(root)
        reached_end = False
        while len(leaves) == 0:
                while len(parents) != 0:
                    parent = parents.pop(0)
                    if parent.right == None or parent.left == None:
                        reached_end = True
                    if reached_end and len(leaves) != 0:
                        while len(leaves) > 0:
                            leaf = leaves.pop(0)
                            if leaf.left != None or leaf.right != None:
                                return False
                            parents.append(leaf)
                    if parent.left != None:
                        if reached_end:
                            if parent.left.left != None or parent.left.right != None:
                                return False
                        leaves.append(parent.left)
                    if parent.right != None:
                        if reached_end:
                                if parent.right.left != None or parent.right.right != None:
                                        return False
                        leaves.append(parent.right)
                if len(parents) == 0 and len(leaves) == 0:
                    return True
                parents = leaves
                leaves = [] 
