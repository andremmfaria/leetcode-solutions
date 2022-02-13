#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
import enum


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if s == p:
            return True
        else:
            for ip, cp in enumerate(p):
                if cp == '*':
                    pass

        
# @lc code=end

