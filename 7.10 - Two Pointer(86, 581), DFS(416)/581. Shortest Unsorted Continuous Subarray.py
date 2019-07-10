'''
Given an integer array, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order, too.
You need to find the shortest such subarray and output its length.

Example 1:
Input: [2, 6, 4, 8, 10, 9, 15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Note:
1.The length of the input array is in range [1, 10,000].
2.The input array may contain duplicates, so ascending order here means <=.
'''

#Brute Force
# idea: 1. Copy array and sort
#       2. Two iter, one from left and one from right. Compare sorted list and original list
#       3. Stop loop until two way are all different. Return length between two iters

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        numsSort = nums[:]
        numsSort.sort()
        
        iterLeft = 0
        iterRight = len(nums) - 1
        
        while iterLeft < iterRight:
            isContinuous = False
            
            if numsSort[iterLeft] == nums[iterLeft]:
                isContinuous = True
                iterLeft += 1
            
            if numsSort[iterRight] == nums[iterRight]:
                isContinuous = True
                iterRight -= 1
                
            if not isContinuous:
                break
                
        if iterLeft == iterRight:
            return 0
        else:
            return iterRight - iterLeft + 1
