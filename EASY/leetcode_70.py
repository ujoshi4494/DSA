# 70. Climbing Stairs
# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

# Solution - 

# Approach - 
# This is classic fibonacci problem where we have to use previous two steps counts to calculate present count

# Example - 
# To calculate no of ways to reach at 4
# You can reach at 4 by either from stair 3rd or stair 2nd (f(n) -> f(n-1) + f(n-2))


class Solution:
    def climbStairs(self, n: int) -> int:
        ans = [1]*(n+1)
        if n<=2:
            return n
        ans[2] = 2
        for i in range(3, n+1):
            # f(n) -> f(n-1) + f(n-2)
            ans[i] = ans[i-1] + ans[i-2]
        return ans[n]