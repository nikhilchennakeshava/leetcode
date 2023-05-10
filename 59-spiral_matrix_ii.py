'''
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

Example 1:

Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:

Input: n = 1
Output: [[1]]

Constraints:

    1 <= n <= 20
'''


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        A, lo = [[n*n]], n*n
        while lo > 1:
            lo, hi = lo - len(A), lo
            A = [list(range(lo, hi))] + list(zip(*A[::-1]))
        return A
