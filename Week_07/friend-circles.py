# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 22:58:02 2020

@author: ZhaoJingjiao
"""

class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M: return 0

        n = len(M)
        p = [i for i in range(n)]
        for i in range(n):
            #此处稍作修改
            for j in range(0,i):
                if M[i][j] == 1:
                    self._union(p, i, j)
        
        return len(set([self._parent(p,i) for i in range(n)]))

    def _union(self, p, i, j):
        p1 = self._parent(p, i)
        p2 = self._parent(p, j)
        p[p1] = p2
    
    def _parent(self, p, i):
        root = i
        while p[root] != root:
            root = p[root]
        while p[i] != i:
            temp = i; i = p[i]; p[temp] = root
        return root

