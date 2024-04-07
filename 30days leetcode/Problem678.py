class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        minop = 0
        maxop = 0

        for i in s:
            if i == "(":
                minop += 1
                maxop += 1
            if i == ")":
                minop -= 1
                maxop -= 1
            if i == '*':
                minop -= 1
                maxop += 1
            if maxop < 0:
                return False
            if minop < 0:
                minop = 0

        return minop == 0




