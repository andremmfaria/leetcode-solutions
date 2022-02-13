#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
from typing import List
import itertools

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if(c == "("): stack.append(c)
            else:
                if(len(stack) == 0): return False
                if(c == ")" and stack[-1] == "("):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        combinations = list(itertools.product("()", repeat=n*2))
        for item in combinations:
            if(self.isValid(item)):
                ans.append("".join(list(item)))

        return ans

# @lc code=end

