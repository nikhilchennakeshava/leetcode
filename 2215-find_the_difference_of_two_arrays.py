class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        n1, n2 = set(nums1), set(nums2)
        return [list(n1-n2), list(n2-n1)]

        # ans = []
        # n1, n2 = set(nums1), set(nums2)
        # ans.append([x for x in n1 if x not in n2])
        # ans.append([x for x in n2 if x not in n1])

        # return ans
