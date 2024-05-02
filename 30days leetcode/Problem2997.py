class Solution(object):
    def minOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        for n in nums:
            k ^= n
        return bin(k).count('1')