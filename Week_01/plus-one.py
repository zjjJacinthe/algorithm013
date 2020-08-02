# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 23:10:39 2020

@author: ZhaoJingjiao
"""


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        digits.insert(0, 1)
        return digits