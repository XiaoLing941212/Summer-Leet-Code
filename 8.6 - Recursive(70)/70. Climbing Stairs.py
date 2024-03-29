'''
You are climbing a stair case. It takes n steps to reach to the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Note: Given n will be a positive integer.

Example 1:
Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 2:
Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''

#Recursive:

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        memo = [0 for i in range(n+1)]
        return self.recurStairs(0, n, memo)
    
    def recurStairs(self, i, n, memo):
        if i > n:
            return 0
        
        if i == n:
            return 1
        
        if memo[i] > 0:
            return memo[i]
        
        memo[i] = self.recurStairs(i + 1, n, memo) + self.recurStairs(i + 2, n, memo)
        return memo[i]
