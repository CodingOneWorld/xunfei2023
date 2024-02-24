# -*- coding: utf-8 -*-
'''
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。



示例 1:

输入: nums = [0,1,0,3,12]
输出: [1,3,12,0,0]

示例 2:

输入: nums = [0]
输出: [0]



提示:

    1 <= nums.length <= 104
    -231 <= nums[i] <= 231 - 1



进阶：你能尽量减少完成的操作次数吗？

https://leetcode.cn/problems/move-zeroes/
'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tem=[]
        for i in range(len(nums)):
            if nums[i]!=0:
                tem.append(nums[i])

        for i in range(len(nums)):
            if i < len(tem):
                nums[i]=tem[i]
            else:
                nums[i]=0


# 移动零
# 第一次遇到非零元素，将非零元素与数组nums[0]互换，第二次遇到非零元素，将非零元素与nums[1]互换，第三次遇到非零元素，将非零元素与nums[2]，以此类推，直到遍历完数组
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] , nums[i]= nums[i] , nums[j]
                j += 1