"""
A ramp in an integer array nums is a pair (i, j) for which i < j and nums[i] <= nums[j]. The width of such a ramp is j - i.

Given an integer array nums, return the maximum width of a ramp in nums. If there is no ramp in nums, return 0.

 

Example 1:

Input: nums = [6,0,8,2,1,5]
Output: 4
Explanation: The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 and nums[5] = 5.
Example 2:

Input: nums = [9,8,1,0,1,9,4,0,4,1]
Output: 7
Explanation: The maximum width ramp is achieved at (i, j) = (2, 9): nums[2] = 1 and nums[9] = 1.
 

Constraints:

2 <= nums.length <= 5 * 104
0 <= nums[i] <= 5 * 104    
"""
#TLE solution
# def maxWidthRamp(self, nums: List[int]) -> int:
#         ramp = 0
#         n = len(nums)
#         for left in range(n-1):
#             for right in range(left+1,n):
#                 width = nums[right] - nums[left]    
#                 if width >= 0 :
#                     ramp = max(ramp, right - left)
#         return ramp
#Optimized solution
from typing import List
class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        indices = [i for i in range(n)]
        indices.sort(key = lambda i :(nums[i],i))
        min_index = n
        max_width = 0
        for i in indices :
            max_width = max(max_width, i - min_index)
            min_index = min(min_index, i)
        return max_width
    
#Use Cases :
if __name__ == "__main__":
    assert Solution().maxWidthRamp([6,0,8,2,1,5]) == 4
    
print("All passed")