# -*- coding: utf-8 -*-
'''
两个整数之间的 汉明距离 指的是这两个数字对应二进制位不同的位置的数目。

给你两个整数 x 和 y，计算并返回它们之间的汉明距离。



示例 1：

输入：x = 1, y = 4
输出：2
解释：
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
上面的箭头指出了对应二进制位不同的位置。

示例 2：

输入：x = 3, y = 1
输出：1



提示：

    0 <= x, y <= 231 - 1

https://leetcode.cn/problems/hamming-distance/description/
'''


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        binx = bin(x)[2:]
        biny = bin(y)[2:]
        print(binx, biny)

        if len(binx) > len(biny):
            biny = '0' * (len(binx) - len(biny)) + biny
        else:
            binx = '0' * (len(biny) - len(binx)) + binx

        print(binx, biny)
        res = 0
        for i in range(len(binx)):
            if binx[i] != biny[i]:
                res += 1

        return res


x = 1
y = 4
so=Solution()
res=so.hammingDistance(x,y)
print(res)