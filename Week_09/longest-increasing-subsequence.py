# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 23:28:14 2020

@author: ZhaoJingjiao
"""

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        size = len(nums)
        if size <= 1:
            return size
        dp = [1] * size
        for i in range(1, size):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)