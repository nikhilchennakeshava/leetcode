class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max(map(sum, accounts))
        
        # max_wealth = 0

        # for l in accounts:
        #     max_wealth = max(max_wealth, sum(l))
        # return max_wealth
