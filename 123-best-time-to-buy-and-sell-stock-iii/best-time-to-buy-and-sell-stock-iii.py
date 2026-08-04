class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        hold1, hold2 = float('-inf'), float('-inf')
        sell1, sell2 = 0, 0
        for price in prices:
            hold1 = max(hold1, -price)
            sell1 = max(sell1, hold1 + price)
            hold2 = max(hold2, sell1 - price)
            sell2 = max(sell2, hold2 + price)
        return sell2