'''
917. Reverse Only Letters

Given a string s, reverse the string according to the following rules:

    All the characters that are not English letters remain in the same position.
    All the English letters (lowercase or uppercase) should be reversed.

Return s after reversing it. 

Example 1:

Input: s = "ab-cd"
Output: "dc-ba"

Example 2:

Input: s = "a-bC-dEf-ghIj"
Output: "j-Ih-gfE-dCba"

Example 3:

Input: s = "Test1ng-Leet=code-Q!"
Output: "Qedo1ct-eeLg=ntse-T!"

Constraints:

    1 <= s.length <= 100
    s consists of characters with ASCII values in the range [33, 122].
    s does not contain '\"' or '\\'.
'''


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = [c for c in s if c.isalpha()]
        return  ''.join([letters.pop() if c.isalpha() else c for c in s])

        # letters = [c for c in s if c.isalpha()]
        # ans = list(s)

        # for i in range(len(ans)):
        #     if ans[i].isalpha():
        #         ans[i] = letters.pop()

        # return ''.join(ans)

        # letters = [x for x in s if x.isalpha()][::-1]
        # rev = list(s)
        # j = 0

        # for i,v in enumerate(rev):
        #     if v.isalpha():
        #         rev[i] = letters[j]
        #         j += 1
        # return ''.join(rev)
