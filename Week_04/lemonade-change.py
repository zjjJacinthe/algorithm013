# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 23:04:26 2020

@author: ZhaoJingjiao
"""

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        for bill in bills:
            if bill == 5:
                five += 1
            elif bill == 10:
                if five < 1: return False
                five -= 1
                ten += 1
            else:
                if ten and five:
                    ten -= 1
                    five -= 1
                elif five > 2:
                    five -= 3
                else: return False
        return True
# Time Complexity: O(N)
# Space Complexity: O(1)