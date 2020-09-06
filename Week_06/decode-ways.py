# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 22:53:15 2020

@author: ZhaoJingjiao
"""


class Solution:
    def numDecodings(self, s: str) -> int:
        size = len(s)
        if size == 0:
            return 0

        dp = [0 for i in range(size + 1)]

        if s[0] == '0':
            return 0
        
        dp[0], dp[1] = 1, 1
        
        for i in range(1, size):
            one = 0
            two = 0
            if (s[i-1] == '1' and s[i] in '0123456789') or (s[i-1] == '2' and s[i] in '0123456'):
                two = dp[i-1]
            if s[i] in '123456789':
                one = dp[i]
            if s[i] == '0' and s[i-1] in '03456789':
                return 0
            dp[i+1] = one+two
        return dp[-1]
