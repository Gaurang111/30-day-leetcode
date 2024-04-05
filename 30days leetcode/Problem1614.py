class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        pcount = 0
        pmax = 0
        if s == "":
            return pcount
        else:
            for i in s:
                if i == "(":
                    pcount += 1
                    pmax = max(pcount, pmax)
                elif i == ")":
                    pcount -= 1

        return pmax