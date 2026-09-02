class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        buy_date, sell_date = 0, 1

        while sell_date < len(prices):
            if prices[buy_date] > prices[sell_date]:
                buy_date = sell_date
                sell_date = buy_date + 1
            else:
                res = max(res, prices[sell_date] - prices[buy_date])
                sell_date += 1
        return res
