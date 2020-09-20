# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 11:11:12 2020

@author: ZhaoJingjiao
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while(n > 0):
            count += 1
            n = n & (n - 1)
        return count