'''
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.
'''

#Two pointer

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        minLength = float('inf')
        left = 0
        curSum = 0
        
        for right in range(len(nums)):
            curSum += nums[right]
            
            while curSum >= s:
                minLength = min(minLength, right - left + 1)
                curSum -= nums[left]
                left += 1
        
        if minLength != float('inf'):
            return minLength
        else:
            return 0
