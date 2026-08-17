class Solution(object):
    def digitFrequencyScore(self, n):
        """
        :type n: int
        :rtype: int
        """
        summ=0
        while n>0:
            rem=n%10
            summ+=rem
            n//=10
        return summ