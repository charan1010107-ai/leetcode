class Solution(object):
    def trimTrailingVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        x=list(s)
        y=len(x)
        vow="aeiouAEIOU"
        for i in range(y-1,-1,-1):
            if x[i] in vow:
                x.pop()
            else:
                break
        return "".join(x)
            