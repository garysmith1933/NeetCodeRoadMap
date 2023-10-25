class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            res = max(price-lowest, res)
        return res

        #Time O(N) Space O(1)