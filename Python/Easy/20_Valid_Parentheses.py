"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""
#the trick to test if the order is followed is to use a stack
class Solution:
    def isValid(self, s: str) -> bool:
        n = len(s)
        st = [] #stack
        open = ['(','[','{']
        x = 0 #number of valid parentheses
        for element in s: 
            if element in open :
                st.append(element)
            else: 
                if len(st) == 0 :
                    return False
                if element == ')':
                    if st[-1] == '(' :
                        st.pop()
                    else : return False
                if element == ']' :
                    if st[-1] == '[' :
                        st.pop()
                    else : return False
                if element == '}' :
                    if st[-1] == '{'  :
                        st.pop()
                    else : return False
        if len(st) == 0 : 
            return True
        else : return False

#Use Cases :
if __name__ == "__main__":
    assert Solution().isValid("()") == True
    assert Solution().isValid("()[]{}") == True
    assert Solution().isValid("(]") == False
    assert Solution().isValid("([])") == True
    assert Solution().isValid("([)]") == False
    assert Solution().isValid("[") == False
    assert Solution().isValid("]") == False    
    assert Solution().isValid("[([]])") == False

print("All passed")