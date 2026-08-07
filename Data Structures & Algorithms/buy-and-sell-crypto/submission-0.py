class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_profit = 0
        min_found = prices[0]
        for p in prices[1:]:
            profit = p - min_found
            min_found = min(min_found, p)
            best_profit = max(best_profit, profit)
        return best_profit
