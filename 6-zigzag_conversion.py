'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows); 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I

Example 3:

Input: s = "A", numRows = 1
Output: "A"

Constraints:

    1 <= s.length <= 1000
    s consists of English letters (lower-case and upper-case), ',' and '.'.
    1 <= numRows <= 1000
'''


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # If we have only one row then we can return the string as it is
        if numRows < 2:
            return s

        # We will create an empty string for each row and then fill each element in each row
        # from row = 0 to row = numRows-1, if we reach bottom (i.e. row = numRows-1)
        # then we move up. Similarly if we reach top, we change direction and move down
        # Finally after filling up all the four rows we join them row0 + row1 +.. numRows

        result = [""] * numRows

        # We start with first row
        row = 0

        for character in s:
            # if we reach top we have to move down
            if row == 0:
                move_down = True
            # if we reach bottom then we have to move up
            elif row == numRows - 1:
                move_down = False

            # Add character to corresponding row
            result[row] += character

            # update the row -> increment by 1 if we move down else, decrement by 1 if we move up.
            row = (row + 1) if move_down else row - 1

        # Finally join all rows and return
        return "".join(result)
