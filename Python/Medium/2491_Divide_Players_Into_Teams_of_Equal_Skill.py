"""
date : October 4, 2024 
You are given a positive integer array skill of even length n where skill[i] denotes the skill of the ith player. Divide the players into n / 2 teams of size 2 such that the total skill of each team is equal.

The chemistry of a team is equal to the product of the skills of the players on that team.

Return the sum of the chemistry of all the teams, or return -1 if there is no way to divide the players into teams such that the total skill of each team is equal.

 

Example 1:

Input: skill = [3,2,5,1,3,4]
Output: 22
Explanation: 
Divide the players into the following teams: (1, 5), (2, 4), (3, 3), where each team has a total skill of 6.
The sum of the chemistry of all the teams is: 1 * 5 + 2 * 4 + 3 * 3 = 5 + 8 + 9 = 22.
Example 2:

Input: skill = [3,4]
Output: 12
Explanation: 
The two players form a team with a total skill of 7.
The chemistry of the team is 3 * 4 = 12.
Example 3:

Input: skill = [1,1,2,3]
Output: -1
Explanation: 
There is no way to divide the players into teams such that the total skill of each team is equal.
 

Constraints:

2 <= skill.length <= 105
skill.length is even.
1 <= skill[i] <= 1000
"""
from typing import List
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        n = len(skill)
        skill = sorted(skill)
        max = skill[0]+skill[n-1]
        summy = skill[0] * skill[n-1] 
        for i in range(1,n //2 ):
            x = skill[i]+skill[n-i-1]
            if x != max : #there is no way to divide the players into teams such that the total skill of each team is equal.
                return -1
            summy += skill[i]*skill[n-i-1]
        return summy
    
### Unit Testing

if __name__ == "__main__":
    assert Solution().dividePlayers([3,2,5,1,3,4]) == 22
    assert Solution().dividePlayers([3,4]) == 12
    assert Solution().dividePlayers([1,1,2,3]) == -1
    assert Solution().dividePlayers([3, 5]) == 15
    assert Solution().dividePlayers([18, 14, 3, 19, 9, 6, 18, 3, 4, 19]) == -1
    assert Solution().dividePlayers([1, 2, 3, 2, 4, 6]) == -1
    assert Solution().dividePlayers([2, 2, 5, 12, 12, 10, 9, 4]) == 133
    

print("All passed")