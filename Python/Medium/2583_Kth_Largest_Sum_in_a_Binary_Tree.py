"""
You are given the root of a binary tree and a positive integer k.

The level sum in the tree is the sum of the values of the nodes that are on the same level.

Return the kth largest level sum in the tree (not necessarily distinct). If there are fewer than k levels in the tree, return -1.

Note that two nodes are on the same level if they have the same distance from the root.

 

Example 1:


Input: root = [5,8,9,2,1,3,7,4,6], k = 2
Output: 13
Explanation: The level sums are the following:
- Level 1: 5.
- Level 2: 8 + 9 = 17.
- Level 3: 2 + 1 + 3 + 7 = 13.
- Level 4: 4 + 6 = 10.
The 2nd largest level sum is 13.
Example 2:


Input: root = [1,2,null,3], k = 1
Output: 3
Explanation: The largest level sum is 3.
 

Constraints:

The number of nodes in the tree is n.
2 <= n <= 105
1 <= Node.val <= 106
1 <= k <= n
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
from collections import deque
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        # Level order traversal that calculates sum of each level
        def level_order_traversal(root):
            result = []
            if not root:
                return result
            
            queue = deque([root])
            while queue:
                level_sum = 0
                for _ in range(len(queue)):  # Process nodes at the current level
                    node = queue.popleft()
                    if node:
                        level_sum += node.val
                        if node.left:
                            queue.append(node.left)
                        if node.right:
                            queue.append(node.right)
                result.append(level_sum)  # Add the sum of the current level to the result list
            
            return result
        
        # Get the sums of all levels
        level_sums = level_order_traversal(root)
        
        # Check if k is valid
        if k > len(level_sums):
            return -1  # Handle case where k is larger than the number of levels
        
        # Sort the sums in descending order and return the kth largest
        level_sums.sort(reverse=True)
        
        return level_sums[k - 1]

### Unit Testing

if __name__ == "__main__":
    # First test case
    root = TreeNode(val=5,
                    left=TreeNode(val=8,
                                  left=TreeNode(val=2,
                                                left=TreeNode(val=4, left=None, right=None),
                                                right=TreeNode(val=6, left=None, right=None)),
                                  right=TreeNode(val=1, left=None, right=None)),
                    right=TreeNode(val=9,
                                   left=TreeNode(val=3, left=None, right=None),
                                   right=TreeNode(val=7, left=None, right=None)))
    assert Solution().kthLargestLevelSum(root, 2) == 13

    # Second test case
    root = TreeNode(val=1,
                    left=TreeNode(val=2,
                                  left=TreeNode(val=3, left=None, right=None),
                                  right=None),
                    right=None)
    assert Solution().kthLargestLevelSum(root, 1) == 3

    # Third test case
    root = TreeNode(val=897935,
                    left=TreeNode(val=796748, left=None, right=None),
                    right=TreeNode(val=528909,
                                   left=None,
                                   right=TreeNode(val=905326,
                                                  left=TreeNode(val=706311,
                                                                left=None,
                                                                right=TreeNode(val=282251,
                                                                               left=None,
                                                                               right=TreeNode(val=139169, left=None, right=None))),
                                                  right=None)))
    assert Solution().kthLargestLevelSum(root, 4) == 706311

    print("All passed")