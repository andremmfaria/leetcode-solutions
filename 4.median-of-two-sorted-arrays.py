#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
import math
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums: List[int] = sorted(nums1+nums2)
        if len(nums) % 2 == 0:
            med: int = math.floor(len(nums)/2)
            return (nums[med]+nums[med-1])/2
        else:
            med: int = math.floor(len(nums)/2)
            return nums[med]
        
# @lc code=end

