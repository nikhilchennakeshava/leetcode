'''
2108. Find First Palindromic String in the Array

Given an array of strings words, return the first palindromic string in the array. If there is no such string, return an empty string "".

A string is palindromic if it reads the same forward and backward.

Example 1:

Input: words = ["abc","car","ada","racecar","cool"]
Output: "ada"
Explanation: The first string that is palindromic is "ada".
Note that "racecar" is also palindromic, but it is not the first.

Example 2:

Input: words = ["notapalindrome","racecar"]
Output: "racecar"
Explanation: The first and only string that is palindromic is "racecar".

Example 3:

Input: words = ["def","ghi"]
Output: ""
Explanation: There are no palindromic strings, so the empty string is returned.

Constraints:

    1 <= words.length <= 100
    1 <= words[i].length <= 100
    words[i] consists only of lowercase English letters.
'''


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        return next((w for w in words if w == w[:: -1]), '')
        
        # for word in words:
        #     l,r = 0,len(word)-1
        #     is_pal = True
        #     while l<=r:
        #         if word[l]!=word[r]:
        #             is_pal = False
        #             break
        #         else:
        #             l += 1
        #             r -= 1
        #     if is_pal: 
        #         return word
        # return ''
