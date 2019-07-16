'''
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]

Explanation: All root-to-leaf paths are: 1->2->5, 1->3
'''

#DFS:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root == None:
            return []
        
        res = []
        self.dfs(root, [str(root.val)], res)
        return res
        
    def dfs(self, node, item, res):
        if node.left == None and node.right == None:
            res.append('->'.join(item))
            return
        
        if node.left:
            item.append(str(node.left.val))
            self.dfs(node.left, item, res)
            item.pop()
        
        if node.right:
            item.append(str(node.right.val))
            self.dfs(node.right, item, res)
            item.pop()
