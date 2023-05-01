class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = []
        l = 0
        for ch in s:
            if ch in char_set:
                char_set = char_set[char_set.index(ch)+1:]
            char_set.append(ch)
            l = max(l, len(char_set))
        return l
