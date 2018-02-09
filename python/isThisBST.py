"""
Tree to Vector = O(n)
Check vector   = O(n)

Solution       = O(n)
"""

""" Node is defined as
class node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
"""

def BSTvec(root, v, n):
    if root is None:
        return

    if root.left is not None:
        n = BSTvec(root.left, v, n)

    n = n+1
    v.append(root.data)

    if root.right is not None:
        n = BSTvec(root.right, v, n)

    return n

def checkBST(root):
    if root is None:
        return True

    vec = []
    n = BSTvec(root, vec, 0)

    for i in range(0, n-1):
        if vec[i] >= vec[i+1]:
            return False
        else:
            i = i+1

    return True
