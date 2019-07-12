'''
Find the sum of all left leaves in a given binary tree.

Example:

    3
   / \
  9  20
    /  \
   15   7

There are two left leaves in the binary tree, with values 9 and 15 respectively. Return 24.
'''

#DFS

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.selectLeave = []
        self.calSum(root)
        return sum(self.selectLeave)
        
    def calSum(self, root):
        if root is None:
            return root
        if root.left is not None and root.left.left is None and root.left.right is None:
            self.selectLeave.append(root.left.val)
            
        root.left = self.calSum(root.left)
        root.right = self.calSum(root.right)
