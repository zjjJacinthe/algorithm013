# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 11:13:21 2020

@author: ZhaoJingjiao
"""

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n-1)) == 0