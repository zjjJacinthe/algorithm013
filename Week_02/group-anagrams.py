# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 22:21:10 2020

@author: ZhaoJingjiao
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        dict = {}
        for item in strs:
            key = tuple(sorted(item))
            dict[key] = dict.get(key, []) + [item]
        return list(dict.values())

# Time Complexity O(n)
# Space Complexity O(n)