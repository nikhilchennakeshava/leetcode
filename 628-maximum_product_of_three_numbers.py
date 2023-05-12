'''
628. Maximum Product of Three Numbers
Easy
3.7K
612
Companies

Given an integer array nums, find three numbers whose product is maximum and return the maximum product.

Example 1:

Input: nums = [1,2,3]
Output: 6

Example 2:

Input: nums = [1,2,3,4]
Output: 24

Example 3:

Input: nums = [-1,-2,-3]
Output: -6

Constraints:

    3 <= nums.length <= 104
    -1000 <= nums[i] <= 1000
'''


class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[0]*nums[1]*nums[-1], nums[-3]*nums[-2]*nums[-1])

        # pos_nums = sorted(list(map(abs, nums)))[:-4:-1]
        # sign = 1

        # for i in pos_nums:
        #     if -1 * i in nums: sign *= -1
        # print(sign, pos_nums)
        # return sign * reduce(lambda x,y: x*y, pos_nums)