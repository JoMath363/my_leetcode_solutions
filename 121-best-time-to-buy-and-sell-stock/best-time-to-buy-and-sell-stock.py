class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if len(prices) < 2:
            return 0

        min_price = prices[0]
        max_price = 0

        for price in prices[1:]:
            if price < min_price:
                min_price = price
            else:
                max_price = max(max_price, price - min_price)

        return max_price
        