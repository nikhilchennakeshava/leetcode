'''
1716. Calculate Money in Leetcode Bank

Hercy wants to save money for his first car. He puts money in the Leetcode bank every day.

He starts by putting in $1 on Monday, the first day. Every day from Tuesday to Sunday, he will put in $1 more than the day before. On every subsequent Monday, he will put in $1 more than the previous Monday.

Given n, return the total amount of money he will have in the Leetcode bank at the end of the nth day.

Example 1:

Input: n = 4
Output: 10
Explanation: After the 4th day, the total is 1 + 2 + 3 + 4 = 10.

Example 2:

Input: n = 10
Output: 37
Explanation: After the 10th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4) = 37. Notice that on the 2nd Monday, Hercy only puts in $2.

Example 3:

Input: n = 20
Output: 96
Explanation: After the 20th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) + (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.

Constraints:

    1 <= n <= 1000
'''


class Solution:
    def totalMoney(self, n: int) -> int:
        weeks, days = divmod(n,7)

        # AP sum = (n/2) * [2a + (n-1)*d]
        # Here we can have 2 APs - one for weekly and one for remaining days
        # Weekly -> 28,35,42 with a = 28, n = weeks, d = 7
        # Daily -> weeks+1, weeks+2 with a = weeks+1, n = days, d = 1
        
        money = (weeks/2) * (2*28 + (weeks-1)*7) + (days/2) * (2*(weeks+1) + (days-1))

        return int(money)

        
        # # Full weeks
        # # for i in range(weeks):
        # #     money += 28 + i*7

        # money += ((weeks/2) * (2*28+ (weeks-1)*7))
        
        # # remaining days
        # money += ((days/2) * (2*(weeks+1)+days-1))

        # return int(money)
