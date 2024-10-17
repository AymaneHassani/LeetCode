"""
You are given an integer num. You can swap two digits at most once to get the maximum valued number.

Return the maximum valued number you can get.

 

Example 1:

Input: num = 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:

Input: num = 9973
Output: 9973
Explanation: No swap.
 

Constraints:

0 <= num <= 108
"""
class Solution:
    def maximumSwap(self, num: int) -> int:
        new_num = list(str(num))
        flag = True
        for i in range(len(new_num)):
            max_1 = max(new_num[i:])
            if max_1 != new_num[i]:
                farthest_max = 0 
                for j in range(i+1,len(new_num)):
                 # if there are many max in new_num[i:] so we need to take the farthest one that would allow us once swaped to inded have the greatest value 
                    if new_num[j] == max_1 :
                        farthest_max = j
                new_num[farthest_max], new_num[i] = new_num[i], new_num[farthest_max]
                break
        s = ''
        for i in range(len(new_num)):
            s += new_num[i]
        return int(s)
#Use Cases :
if __name__ == "__main__":
    assert Solution().maximumSwap(2736) == 7236
    assert Solution().maximumSwap(9973) == 9973
    assert Solution().maximumSwap(98368) == 98863
    assert Solution().maximumSwap(1993) == 9913

print("All passed")