class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0: return 0

        return num.bit_length() - 1 + num.bit_count()

        # count = 0
        # while num!=0:
        #     if num%2==0: 
        #         num /= 2
        #     else: 
        #         num -= 1
        #     count += 1
        # return count
