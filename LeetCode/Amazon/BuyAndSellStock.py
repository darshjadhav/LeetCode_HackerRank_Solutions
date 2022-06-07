# LEETCODE 121
# Time: O(n), Space: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        l, r = 0, 1 # Buy, Sell
        pMax = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                pMax = max(pMax, profit)
            else:
                l = r

            r += 1

        return pMax
