# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 23:40:40 2020

@author: ZhaoJingjiao
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not (preorder and inorder):
            return None
        root = TreeNode(preorder[0])
        mid_id = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid_id+1], inorder[0:mid_id])
        root.right = self.buildTree(preorder[mid_id+1:], inorder[mid_id+1:])
        return root
# Time Complexity O(n^2) ---- index()
# Space Complexity O(n)
