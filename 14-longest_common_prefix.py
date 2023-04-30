class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ''
        strs = sorted(strs)
        first = strs[0]
        last = strs[-1]

        for i in range(min(len(first), len(last))):
            if first[i]!=last[i]:
                return prefix
            prefix += first[i]
        return prefix

        # prefix = ''
        # char = ''
        # end = False
        # for i in range(len(strs)):
        #     char = strs[0][i]
        #     for str in strs:
        #         if str[i] != char:
        #             end = True
        #             break
        #     if end == True: break
        #     prefix += char
        # return prefix        
