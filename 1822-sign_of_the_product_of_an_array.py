class Solution:
    def arraySign(self, nums: List[int]) -> int:
        p = prod(nums)
        return 1 if p > 0 else -1 if p < 0 else 0
