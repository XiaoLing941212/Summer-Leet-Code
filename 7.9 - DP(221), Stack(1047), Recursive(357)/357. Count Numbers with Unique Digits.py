'''
Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10n.

Example:

Input: 2
Output: 91 
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, 
             excluding 11,22,33,44,55,66,77,88,99
'''

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        return self.Recur(n)
    
    def Recur(self, n):
        if n > 10:
            return self.Recur(10)
        if n == 0:
            return 1
        if n == 1:
            return 10
        
        cur = 1
        for i in range(n):
            cur *= 10 - i
        
        temp = 1
        for i in range(n-1):
            temp *= 9 - i
        
        return cur - temp + self.Recur(n-1)
