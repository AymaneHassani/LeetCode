"""
Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

 

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
Example 2:

Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.
 

Constraints:

1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1

"""
#TLE
class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        import numpy as np
        sq_ma = 0
        row = len(matrix)
        col = len(matrix[0])
        for i in range(row):
            for j in range(col):
                for l in range(min(row,col)+1):
                    sub_matrix = [row[j:j+l] for row in matrix[i:i+l]] 
                    if np.array_equal(sub_matrix, np.ones((l, l))) :
                        sq_ma += 1
        return sq_ma