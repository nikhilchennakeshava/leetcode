'''
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote. 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true

Constraints:

    1 <= ransomNote.length, magazine.length <= 105
    ransomNote and magazine consist of lowercase English letters.
'''


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # note_dict = Counter(ransomNote)
        # magazine_dict = Counter(magazine)
        # return note_dict & magazine_dict == note_dict
      
        # Solution 1
        my_dict = {}
        for c in magazine:
            if c not in my_dict:
                my_dict[c] = 1
            else:
                my_dict[c] += 1
        
        for c in ransomNote:
            if c not in my_dict:
                return False
            else:
                if my_dict[c] > 1:
                    my_dict[c] -= 1
                else:
                    my_dict.pop(c)
        
        return True
