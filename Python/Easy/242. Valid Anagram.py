"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:

Input: s = "anagram", t = "nagaram"

Output: true

Example 2:

Input: s = "rat", t = "car"

Output: false

 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""
from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # After creating two dictinaries to make the count of each letter in s and t, we will compare the two ! 
        letters_of_s = {}
        letters_of_t = {}
        for i in s : 
            if i not in letters_of_s :
                letters_of_s[i] = 0
            letters_of_s[i] += 1
        for i in t : 
            if i not in letters_of_t :
                letters_of_t[i] = 0
            letters_of_t[i] += 1
            return letters_of_s == letters_of_t
    
    #A shorther version would use the method counter from collections
    def isAnagram_2(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

if __name__ == "__main__" :
    assert Solution().isAnagram("anaégram:,","nagaramé:,") == True
    assert Solution().isAnagram("rat", "cat") == False
    assert Solution().isAnagram("aa", "a") == False #remember in an anagram s is just a random organisation of t, and shouldn't have more or less letters
    
    assert Solution().isAnagram_2("anagram","nagaram") == True
    assert Solution().isAnagram_2("rat", "cat") == False
    assert Solution().isAnagram_2("aa", "a") == False #remember in an anagram s is just a random organisation of t, and shouldn't have more or less letters

print("All passed")
    