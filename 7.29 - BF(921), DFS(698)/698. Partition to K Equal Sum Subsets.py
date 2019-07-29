'''
Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

Example 1:
Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.
'''

#DFS:

class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        l = len(nums)
        s = sum(nums)
        
        #cannot perfectly divided
        if s % k != 0:
            return False
        
        target = s // k
        targets = [target] * k
        
        nums.sort(reverse = True)
        #if target less than first element, then false
        if target < nums[0]:
            return False
        
        def dfs(pos):
            if pos == l:
                return True
            
            for i in range(k):
                if targets[i] >= nums[pos]:
                    targets[i] -= nums[pos]
                    
                    if 0 < targets[i] < nums[-1]:
                        targets[i] += nums[pos]
                        continue
                    if dfs(pos + 1):
                        return True
                    targets[i] += nums[pos]
            
            return False
        
        return dfs(0)
        
