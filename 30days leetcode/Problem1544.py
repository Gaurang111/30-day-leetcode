class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        mystack = []
        for i in s:
            if mystack and abs(ord(i) - ord(mystack[-1])) == 32:
                mystack.pop()
            else:
                mystack.append(i)

        return ''.join(mystack)
