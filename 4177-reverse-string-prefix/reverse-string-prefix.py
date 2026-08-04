class Solution(object):
    def reversePrefix(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        x=s[:k]
        x=x[::-1]
        return x+s[k:]