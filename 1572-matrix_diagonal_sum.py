'''
1572. Matrix Diagonal Sum

Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal. 

Example 1:

Input: mat = [[1,2,3],
              [4,5,6],
              [7,8,9]]
Output: 25
Explanation: Diagonals sum: 1 + 5 + 9 + 3 + 7 = 25
Notice that element mat[1][1] = 5 is counted only once.

Example 2:

Input: mat = [[1,1,1,1],
              [1,1,1,1],
              [1,1,1,1],
              [1,1,1,1]]
Output: 8

Example 3:

Input: mat = [[5]]
Output: 5

Constraints:

    n == mat.length == mat[i].length
    1 <= n <= 100
    1 <= mat[i][j] <= 100
'''


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n, ans = len(mat)-1, 0

        for i in range(len(mat)):
            ans += mat[i][i] + mat[i][n-i]

        if mod(n, 2) == 0: ans -= mat[n//2][n//2]
        return ans
        
        # i, j, ans = 0, len(mat)-1, 0

        # while i < len(mat):
        #     if i==j:
        #         ans += mat[i][j]
        #     else:
        #         ans += mat[i][i] + mat[i][j]
        #     i += 1
        #     j -= 1

        # return ans
