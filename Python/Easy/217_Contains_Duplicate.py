"""217. Contains Duplicate
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true


Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

# A set in pythons would remove all redondant element, we can then compare the length of each one
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        set_nums = set(nums)
        m = len(set_nums)
        if n != m :
            return True
        return False

#Use Cases :
if __name__ == "__main__":
    assert Solution().containsDuplicate([1,2,3,1]) == True
    assert Solution().containsDuplicate([1,2,3,4]) == False
    assert Solution().containsDuplicate([1,1,1,3,3,4,3,2,4,2]) == True
    
print("All passed")