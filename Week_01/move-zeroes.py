# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 22:57:35 2020

@author: ZhaoJingjiao
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(0, len(nums)):
            if nums[i] != 0:
                if i != j:
                    nums[j], nums[i] = nums[i], nums[j]
                j += 1
