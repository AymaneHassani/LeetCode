"""
Given two strings s1 and s2, return true if s2 contains a 
permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        x = {}
        n1 = len(s1)
        n2 = len(s2)
        for i in range(n1):
            if s1[i] not in x :
                x[s1[i]] = 0
            x[s1[i]] +=1
        for j in range(n2-n1+1):
            y = {}
            for i in range(j,j+n1):
                if s2[i] not in y:
                    y[s2[i]] = 0
                y[s2[i]] += 1
            if y == x :
                return True
        return False
    
### Unit Testing

if __name__ == "__main__":
    assert Solution().checkInclusion("ab","eidbaooo") == True
    assert Solution().checkInclusion("ab","eidboaoo") == False
    assert Solution().checkInclusion("adc","dcda") == True
    assert Solution().checkInclusion("abc","ccccbbbbaaaa") == False
    

print("All passed")