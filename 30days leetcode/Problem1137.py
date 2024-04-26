class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        first, second, third = 0, 1, 1

        if n == 0:
            return first
        elif n == 1 or n == 2:
            return second
        ans = 0
        for i in range(3, n + 1):
            ans = first + second + third
            first, second, third = second, third, ans

        return ans