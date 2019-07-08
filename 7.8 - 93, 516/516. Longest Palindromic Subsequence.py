'''
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input: "bbbab"
Output: 4
One possible longest palindromic subsequence is "bbbb".

Example 2:
Input: "cbbd"
Output: 2
One possible longest palindromic subsequence is "bb".
'''

#DP:
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        l = len(s)
        if l == 1 or l == 0:
            return l
        
        #initial index matrix and set all elements to 1
        resultMatrix = [[1]*l for i in range(l)]
        
        #apply dynamics programming
        for a in range(1, l):
            for i in range(0, l - a):
                j = i + a
            
                if s[i] == s[j] and a == 1:
                    resultMatrix[i][j] = 2
                elif s[i] == s[j]:
                    resultMatrix[i][j] = 2 + resultMatrix[i+1][j-1]
                else:
                    resultMatrix[i][j] = max(resultMatrix[i][j-1], resultMatrix[i+1][j])
                
        return resultMatrix[0][l-1]
