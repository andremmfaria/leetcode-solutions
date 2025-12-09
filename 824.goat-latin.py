#
# @lc app=leetcode id=824 lang=python3
#
# [824] Goat Latin
#
# https://leetcode.com/problems/goat-latin/description/
#
# algorithms
# Easy (69.68%)
# Likes:    1006
# Dislikes: 1298
# Total Accepted:    235.5K
# Total Submissions: 337.5K
# Testcase Example:  '"I speak Goat Latin"'
#
# You are given a string sentence that consist of words separated by spaces.
# Each word consists of lowercase and uppercase letters only.
# 
# We would like to convert the sentence to "Goat Latin" (a made-up language
# similar to Pig Latin.) The rules of Goat Latin are as follows:
# 
# 
# If a word begins with a vowel ('a', 'e', 'i', 'o', or 'u'), append "ma" to
# the end of the word.
# 
# 
# For example, the word "apple" becomes "applema".
# 
# 
# If a word begins with a consonant (i.e., not a vowel), remove the first
# letter and append it to the end, then add "ma".
# 
# For example, the word "goat" becomes "oatgma".
# 
# 
# Add one letter 'a' to the end of each word per its word index in the
# sentence, starting with 1.
# 
# For example, the first word gets "a" added to the end, the second word gets
# "aa" added to the end, and so on.
# 
# 
# 
# 
# Return the final sentence representing the conversion from sentence to Goat
# Latin.
# 
# 
# Example 1:
# Input: sentence = "I speak Goat Latin"
# Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"
# Example 2:
# Input: sentence = "The quick brown fox jumped over the lazy dog"
# Output: "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa
# hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
# 
# 
# Constraints:
# 
# 
# 1 <= sentence.length <= 150
# sentence consists of English letters and spaces.
# sentence has no leading or trailing spaces.
# All the words in sentence are separated by a single space.
# 
# 
#

# @lc code=start
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        words_sentence = sentence.split()
        vowels = set("aeiouAEIOU")
        suffix = "a"

        for index, word in enumerate(words_sentence):
            if word[0] in vowels : # Rule vowel
                word += "ma"
            else: # Rule consonant
                word = f"{word[1:]}{word[0]}ma"
            # Rule append a 
            word += suffix
            words_sentence[index] = word
            suffix += "a"   # grow the 'a' suffix for the next word
        
        return " ".join(words_sentence)
        
# @lc code=end

