class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        rev = int(str(abs(x))[::-1])
        num = rev * sign
        return 0 if num > pow(2, 31) or num < -1 * pow(2,31) else num
