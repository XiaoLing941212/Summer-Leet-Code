'''
Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
 
Example 1:
Input: [1, 5, 11, 5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].
 
Example 2:
Input: [1, 2, 3, 5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
'''

#DFS(Note: Search from large to small will reduce run time)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # idea:
        # 1. Sum is odd, cannot partition
        # 2. Sum is even, target would be Sum/2
        # 3. DFS
        
        l = len(nums)
        
        #not enough elements
        if l == 0:
            return True
        elif l == 1:
            return False
        
        s = sum(nums)
        
        #sum is odd, false
        if s % 2 == 1:
            return False
        
        result = s // 2
        
        #largest element larger than result, false
        if max(nums) > result:
            return False
        
        nums.sort(reverse=True)
        return self.dfs(nums, result, 0)
    
    def dfs(self, nums, result, idx):
        if result == 0:
            return True
        elif result < 0:
            return False
        else:
            for i in range(idx, len(nums)):
                if self.dfs(nums, result - nums[i], i+1):
                    return True
            
            return False
