class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest_palindrome = (0, 1)
        dp = [[0]*len(s) for _ in range(len(s))]
        # filling out the diagonal with True
        for i in range(len(s)):
            dp[i][i] = True
			
        # filling the dp table
        for i in range(len(s)-1,-1,-1):
				# j starts from the i location : to only work on the upper side of the diagonal 
            for j in range(i+1,len(s)):  
                if s[i] == s[j]:  # if the chars mathces
                    # if len sliced sub_string is just one letter if the characters are equal, we can say they are palindrome dp[i][j] =True 
                    # if the sliced sub_string is longer than 1, then we should check if the inner string is also palindrome (check dp[i+1][j-1] is True)
                    if j-i == 1 or dp[i+1][j-1] is True:
                        dp[i][j] = True
                        # we also need to keep track of the maximum palindrom sequence 
                        if longest_palindrome[1] - longest_palindrome[0] < j - i + 1:
                            longest_palindrome = (i, j+1)
                
        return s[longest_palindrome[0]:longest_palindrome[1]]
