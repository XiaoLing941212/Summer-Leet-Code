'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
'''

#DFS
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        
        nums.sort()
        
        def dfs(nums, path, result):
            if nums == []:
                result.append(path)
                return
            
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                else:
                    dfs(nums[:i] + nums[i+1:], path + [nums[i]], result)
        
        dfs(nums, path, result)
        return result
