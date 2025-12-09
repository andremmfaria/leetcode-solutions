#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#
# https://leetcode.com/problems/integer-to-roman/description/
#
# algorithms
# Medium (69.63%)
# Likes:    8278
# Dislikes: 5702
# Total Accepted:    2M
# Total Submissions: 2.8M
# Testcase Example:  '3749'
#
# Seven different symbols represent Roman numerals with the following
# values:
# 
# 
# 
# 
# Symbol
# Value
# 
# 
# 
# 
# I
# 1
# 
# 
# V
# 5
# 
# 
# X
# 10
# 
# 
# L
# 50
# 
# 
# C
# 100
# 
# 
# D
# 500
# 
# 
# M
# 1000
# 
# 
# 
# 
# Roman numerals are formed by appending the conversions of decimal place
# values from highest to lowest. Converting a decimal place value into a Roman
# numeral has the following rules:
# 
# 
# If the value does not start with 4 or 9, select the symbol of the maximal
# value that can be subtracted from the input, append that symbol to the
# result, subtract its value, and convert the remainder to a Roman numeral.
# If the value starts with 4 or 9 use the subtractive form representing one
# symbol subtracted from the following symbol, for example, 4 is 1 (I) less
# than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following
# subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and
# 900 (CM).
# Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times
# to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D)
# multiple times. If you need to append a symbol 4 times use the subtractive
# form.
# 
# 
# Given an integer, convert it to a Roman numeral.
# 
# 
# Example 1:
# 
# 
# Input: num = 3749
# 
# Output: "MMMDCCXLIX"
# 
# Explanation:
# 
# 
# 3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
# ⁠700 = DCC as 500 (D) + 100 (C) + 100 (C)
# ⁠ 40 = XL as 10 (X) less of 50 (L)
# ⁠  9 = IX as 1 (I) less of 10 (X)
# Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on
# decimal places
# 
# 
# 
# Example 2:
# 
# 
# Input: num = 58
# 
# Output: "LVIII"
# 
# Explanation:
# 
# 
# 50 = L
# ⁠8 = VIII
# 
# 
# 
# Example 3:
# 
# 
# Input: num = 1994
# 
# Output: "MCMXCIV"
# 
# Explanation:
# 
# 
# 1000 = M
# ⁠900 = CM
# ⁠ 90 = XC
# ⁠  4 = IV
# 
# 
# 
# 
# Constraints:
# 
# 
# 1 <= num <= 3999
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def intToRoman(self, num: int) -> str:
        # Build decimals (thousands, hundreds, tens, ones) as place values
        num_str = str(num)
        decimals: List[int] = []
        for index in range(len(num_str) - 1, -1, -1):
            decimals.append(int(num_str[index]) * pow(10, len(num_str) - 1 - index))
        decimals.reverse()

        # Helper converts a single place value using its (one, five, ten) symbols
        def convert_place(value: int, one: str, five: str, ten: str) -> str:
            d = value // (1 if one == "I" else (10 if one == "X" else (100 if one == "C" else 1000)))
            # d is the digit for this place (0..9), but for thousands it's 0..3
            if one == "M":
                return "M" * d
            if d == 0:
                return ""
            if d <= 3:
                return one * d
            if d == 4:
                return one + five
            if d == 5:
                return five
            if 6 <= d <= 8:
                return five + one * (d - 5)
            # d == 9
            return one + ten

        res: List[str] = []
        for val in decimals:
            if val >= 1000:
                res.append(convert_place(val, "M", "", ""))
            elif val >= 100:
                res.append(convert_place(val, "C", "D", "M"))
            elif val >= 10:
                res.append(convert_place(val, "X", "L", "C"))
            else:
                res.append(convert_place(val, "I", "V", "X"))
        return "".join(res)
        
# @lc code=end
