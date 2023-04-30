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
