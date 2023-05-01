class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        for i,num in enumerate(nums):
            if target-num in my_dict:
                return [i, my_dict[target-num]]
            my_dict[num] = i
