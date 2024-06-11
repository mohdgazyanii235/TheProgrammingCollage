# problem url - https://leetcode.com/problems/longest-palindromic-substring/description/

class Solution:

    def isPalindrome(self, s: str) -> bool:
        rev_s = s[::-1]
        return s == rev_s


    def longestPalindrome(self, s: str) -> str:

        max_length = 0
        max_palindrome = ""

        i = 0
        while i < len(s):
            j = i
            while j < len(s):
                current_substring = s[i:j+1]
                if self.isPalindrome(current_substring) and len(current_substring) > max_length:
                    max_length = len(current_substring)
                    max_palindrome = current_substring
                j += 1
            i += 1

        return max_palindrome
