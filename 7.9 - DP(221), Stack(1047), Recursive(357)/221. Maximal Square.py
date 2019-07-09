'''
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:

Input: 

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
'''

#DP
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row = len(matrix)
        if matrix == []:
            col = 0
        else:
            col = len(matrix[0])
        
        #initial DP matrix with all 0's.
        dpMatrix = [[0]*col for i in range(row)]
        
        #define max length      
        maxLength = 0
        
        #First column and first row same as input matrix
        for i in range(row):
            dpMatrix[i][0] = int(matrix[i][0])
            
            if matrix[i][0] == '1':
                maxLength = 1

        for i in range(col):
            dpMatrix[0][i] = int(matrix[0][i])

            if matrix[0][i] == '1':
                maxLength = 1
       
        #Use dynamics programming to compute largest length
        #######################################################
        #                 i,j starts from 1                   #
        #            if i,j is 0, then DP[i,j] is 0           #
        #       if i,j is 1, then DP[i,j] is minimum of       #
        #DP[i-1,j], DP[i,j-1], and DP[i-1,j-1] if i-1,j-1 is 1#
        #            DP[i,j] is 1 if i-1, j-1 is 0            #
        #######################################################

        for i in range(1, row):
            for j in range(1, col):
                if matrix[i][j] == '1':
                    if matrix[i-1][j-1] == '0':
                        dpMatrix[i][j] = 1
                    else:
                        dpMatrix[i][j] = min(dpMatrix[i-1][j], dpMatrix[i][j-1], dpMatrix[i-1][j-1]) + 1
                    
                    if dpMatrix[i][j] > maxLength:
                        maxLength = dpMatrix[i][j]
                    
                else:
                    dpMatrix[i][j] = 0
                    
        return maxLength * maxLength
