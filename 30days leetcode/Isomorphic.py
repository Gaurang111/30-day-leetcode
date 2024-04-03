class Solution(object):

    def isIsomorphic(self, s, t):

        mydict = {}
        for i in range(len(s)):
            if mydict.get(s[i]) is not None:
                if mydict.get(s[i]) != t[i]:
                    return False
            else:
                mydict[s[i]] = t[i]

        if len(mydict.values()) != len(set(mydict.values())):
            return False

        return True
