class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        res=0
        for i in range(len(stones)):
            if stones[i] in jewels:
                res=res+1
        return res