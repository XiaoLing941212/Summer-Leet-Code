'''
Two images A and B are given, represented as binary, square matrices of the same size.  (A binary matrix has only 0s and 1s as values.)
We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.  After, the overlap of this translation is the number of positions that have a 1 in both images.
(Note also that a translation does not include any kind of rotation.)
What is the largest possible overlap?

Example 1:
Input: A = [[1,1,0],
            [0,1,0],
            [0,1,0]]
       B = [[0,0,0],
            [0,1,1],
            [0,0,1]]
Output: 3
Explanation: We slide A to right by 1 unit and down by 1 unit.
'''

#Collection.Counter:

class Solution(object):
    def largestOverlap(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        r = len(A)
        c = len(A[0])
        
        prevA = []
        newB = []
        
        for i in range(r):
            for j in range(c):
                if A[i][j] == 1:
                    prevA.append((i, j))
                if B[i][j] == 1:
                    newB.append((i, j))
        
        v = collections.Counter()
        
        for ax, ay in prevA:
            for bx, by in newB:
                k = (ax - bx, ay - by)
                v[k] += 1
        
        return max(v.values() or [0])
