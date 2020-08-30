# -*- coding:utf-8 -*-

class Finder:
    def findKth(self, a, n, K):
        a.sort(reverse=True)
        return a[K-1]