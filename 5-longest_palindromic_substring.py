class Solution:
    def longestPalindrome(self, s: str) -> str:
        # # DP 3
        # dp = [[0]*len(s) for _ in range(len(s))]
        # for i in range(len(s)):
        #     dp[i][i] = 1

        # max_l = 0
        # loc = (0,1)

        # if len(s) < 2: return s
        
        # for i in range(len(s)-1,-1,-1):
        #     # j starts from the i location : to only work on the upper side of the diagonal 
        #     for j in range(i+1,len(s)):
        #         if s[i]==s[j]:
        #             if j-i==1:
        #                 dp[i][i] = 2
        #                 continue
        #             if dp[i+1][j-1]:
        #                 dp[i][j] = 2 + dp[i+1][j-1] 
        #         if max_l < j-i+1:
        #             max_l = j-i+1
        #             loc = (i+1, j)
        # return s[loc[0]:loc[1]]

        # # DP 2
        # dp = [[False]*len(s) for _ in range(len(s))]
        # for i in range(len(s)):
        #     dp[i][i]=True
        # res = s[0]
        # for j in range(len(s)):
        #     for i in range(j):
        #         if s[i]==s[j] and (dp[i+1][j-1] or j==i+1):
        #             dp[i][j] = True
        #             if j-i+1 > len(res):
        #                 res = s[i:j+1]
        # return res
        
        # Expanding approach
        str_length, max_len, start = len(s), 0, 0

        for i in range(str_length):
            for left,right in [(i,i),(i,i+1)]:
                while left >= 0 and right < str_length and s[left] == s[right]:
                    left -= 1
                    right += 1
                if right - left - 1 > max_len: 
                    max_len = right - left - 1
                    start = left + 1
        return s[start:start+max_len]

        # # DP 1
        # longest_palindrome = (0, 1)
        # dp = [[0]*len(s) for _ in range(len(s))]
        # # filling out the diagonal with True
        # for i in range(len(s)):
        #     dp[i][i] = True
			
        # # filling the dp table
        # for i in range(len(s)-1,-1,-1):
		# 		# j starts from the i location : to only work on the upper side of the diagonal 
        #     for j in range(i+1,len(s)):  
        #         if s[i] == s[j]:  # if the chars mathces
        #             # if len sliced sub_string is just one letter if the characters are equal, we can say they are palindrome dp[i][j] =True 
        #             # if the sliced sub_string is longer than 1, then we should check if the inner string is also palindrome (check dp[i+1][j-1] is True)
        #             if j-i == 1 or dp[i+1][j-1] is True:
        #                 dp[i][j] = True
        #                 # we also need to keep track of the maximum palindrom sequence 
        #                 if longest_palindrome[1] - longest_palindrome[0] < j - i + 1:
        #                     longest_palindrome = (i, j+1)
                
        # return s[longest_palindrome[0]:longest_palindrome[1]]
