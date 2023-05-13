'''
387. First Unique Character in a String

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:

Input: s = "leetcode"
Output: 0

Example 2:

Input: s = "loveleetcode"
Output: 2

Example 3:

Input: s = "aabb"
Output: -1

Constraints:

    1 <= s.length <= 105
    s consists of only lowercase English letters.
'''


class Solution:
    def firstUniqChar(self, s: str) -> int:
        count_dict = {}
        for ch in s:
            count_dict[ch] = count_dict.get(ch, 0) + 1

        for i in range(len(s)):
            if count_dict[s[i]] == 1: return i
        return -1

        # count_dict = {}
        # for ch in s:
        #     count_dict[ch] = count_dict.get(ch, 0) + 1

        # for ch in count_dict:
        #     if count_dict[ch] == 1: return s.find(ch)
        # else:
        #     return -1
