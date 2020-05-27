#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
#
# algorithms
# Easy (49.99%)
# Likes:    4651
# Dislikes: 208
# Total Accepted:    817.7K
# Total Submissions: 1.6M
# Testcase Example:  '[7,1,5,3,6,4]'
#
# Say you have an array for which the i^th element is the price of a given
# stock on day i.
#
# If you were only permitted to complete at most one transaction (i.e., buy one
# and sell one share of the stock), design an algorithm to find the maximum
# profit.
#
# Note that you cannot sell a stock before you buy one.
#
# Example 1:
#
#
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit =
# 6-1 = 5.
# Not 7-1 = 6, as selling price needs to be larger than buying price.
#
#
# Example 2:
#
#
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
#
#
#

# @lc code=start
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        This implementation is an O(n) solution for maxProfit using pointers.
        Like twoSum, the naive brute-force solution (ie two loops, with i < j <
        len(prices), and computing maximum for all combinations of prices[j] -
        prices[i]) has an O(n^2) solution. 

        For maxProfit, we only need to keep track of two variables: the minimum
        price at and the maximum profit up to some point i. Yielding the
        maximum profit will, trivially, invole buying stock at the lowest
        price, which motivates why we keep track of the minumum price. Then, we
        keep track of the largest margin between an price at day j (in the
        future) and the minumum price. 
        """
        min_price = float("inf")
        max_profit = 0
        for p in prices:
            min_price = min(min_price, p)
            max_profit = max(max_profit, p - min_price)
        return max_profit


if __name__ == "__main__":
    s = Solution()
    assert s.maxProfit([7, 1, 5, 3, 6, 4]) == 5
    assert s.maxProfit([7, 6, 4, 3, 1]) == 0
# @lc code=end
