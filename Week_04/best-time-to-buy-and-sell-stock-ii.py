# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 23:18:58 2020

@author: ZhaoJingjiao
"""


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        len_prices = len(prices)
        if len_prices == 0:
            return 0
        for i in range(1, len_prices):
            tmp = prices[i] - prices[i-1]
            if tmp > 0:
                max_profit += tmp
        return max_profit

# Time Complexity: O(N)
# Space Complexity: O(1)