'''
463. Island Perimeter

You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island. 

Example 1:

Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.

Example 2:

Input: grid = [[1]]
Output: 4

Example 3:

Input: grid = [[1,0]]
Output: 4

Constraints:

    row == grid.length
    col == grid[i].length
    1 <= row, col <= 100
    grid[i][j] is 0 or 1.
    There is exactly one island in grid.
'''


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m = len(grid)+2
        n = len(grid[0])+2

        for i in range(len(grid)):
            grid[i].insert(0,0)
            grid[i].append(0)
        grid.insert(0,[0]*n)
        grid.append([0]*n)

        return sum(4-grid[i][j-1]-grid[i-1][j]-grid[i][j+1]-grid[i+1][j] for i in range(1,m-1) for j in range(1,n-1) if grid[i][j])
