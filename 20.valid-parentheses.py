#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if(c == "(" or c == "{" or c == "["):
                stack.append(c)
            else:
                if(len(stack) == 0):
                    return False
                if(c == ")" and stack[-1] == "("):
                    stack.pop()
                elif(c == "}" and stack[-1] == "{"):
                    stack.pop()
                elif(c == "]" and stack[-1] == "["):
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
        
# @lc code=end

