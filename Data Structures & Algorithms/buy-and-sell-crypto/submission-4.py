class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0             # store the max profit here
        l = 0
        r = l + 1           # the right pointer starts right next to the left pointer as time is linear

        while r < len(prices):
            if prices[l] > prices[r]:
                l = r       # make sure the left pointer is at the min
                r = r + 1
            else:
                res = max(res, prices[r] - prices[l])
                r = r + 1

        return res
        