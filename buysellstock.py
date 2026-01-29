class Solution(object):
    def maxProfit(self, prices):
        buy = max(prices)
        sell = 0
        for i in range(len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif (prices[i] - buy ) > sell:
                sell = prices[i] - buy
        return sell
        
