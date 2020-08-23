# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 23:52:45 2020

@author: ZhaoJingjiao
"""

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        s_point, g_point = 0, 0
        while s_point < len(s) and g_point < len(g):
            if s[s_point] >= g[g_point]:
                g_point += 1
            s_point += 1
        return g_point
# Time Complexity: O(n)
# Space Complexity: O(1)