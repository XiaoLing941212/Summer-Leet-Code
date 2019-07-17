'''
A full binary tree is a binary tree where each node has exactly 0 or 2 children.
Return a list of all possible full binary trees with N nodes.  Each element of the answer is the root node of one possible tree.
Each node of each tree in the answer must have node.val = 0.
You may return the final list of trees in any order.

Example 1:
Input: 7
Output: [[0,0,0,null,null,0,0,null,null,0,0],[0,0,0,null,null,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,null,null,null,null,0,0],[0,0,0,0,0,null,null,0,0]]
'''

#Recursive:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.memo = {}
    
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        if N in self.memo:
            return self.memo[N]
        if N == 0:
            return []
        if N == 1:
            return [TreeNode(0)]
        
        res = []
        for i in range(1, N):
            left, right = self.allPossibleFBT(i), self.allPossibleFBT(N-1-i)
            
            for l in left:
                for r in right:
                    root = TreeNode(0)
                    root.left = l
                    root.right = r
                    res.append(root)
        
        self.memo[N] = res
        return self.memo[N]
