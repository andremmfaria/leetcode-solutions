#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
import itertools
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz"
        }
        ans = []

        if digits:
            str_combinations: List[str] = [mapping[int(num)] for num in digits]
            ans += ["".join(i) for i in itertools.product(*str_combinations)]
            return ans
        else:
            return ans
        
        # lenD, ans = len(digits), []
        # if digits == "": return []
        # def bfs(pos: int, st: str):
        #     if pos == lenD: ans.append(st)
        #     else:
        #         letters = mapping[digits[pos]]
        #         for letter in letters:
        #             bfs(pos+1,st+letter)
        # bfs(0,"")
        # return ans

# @lc code=end

