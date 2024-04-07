class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        sl = list(s)
        openp = 0
        for i, char in enumerate(sl):
            if sl[i] == "(":
                openp += 1
            if sl[i] == ")":
                if openp > 0:
                    openp -= 1
                else:
                    sl[i] = ''

        if openp > 0:
            for i in range(len(s) - 1, -1, -1):
                if sl[i] == "(":
                    openp -= 1
                    sl[i] = ''

                if openp == 0:
                    return ''.join(sl)

        return ''.join(sl)