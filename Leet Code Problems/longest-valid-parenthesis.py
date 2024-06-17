# problem url - https://leetcode.com/problems/longest-valid-parentheses/description/

class Solution:

    def find_largest_gap(self, parenthesis_stack, s):
        low = 0
        high = 1
        current_max = 0
        parenthesis_stack.insert(0, -1)
        parenthesis_stack.append(len(s))
        while high < len(parenthesis_stack):
            temp_lenght = parenthesis_stack[high] - (parenthesis_stack[low]+1)
            if temp_lenght >  current_max:
                current_max = temp_lenght
            low += 1
            high += 1

        return current_max



    def longestValidParentheses(self, s: str) -> int:
        parenthesis_stack = []

        i = 0
        while i < len(s):
            if s[i] == "(":
                parenthesis_stack.append(i)
            else:
                if not parenthesis_stack or s[parenthesis_stack[-1]] == ")":
                    parenthesis_stack.append(i)
                elif s[parenthesis_stack[-1]] == "(":
                    parenthesis_stack.pop()
            i += 1

        return self.find_largest_gap(parenthesis_stack, s)

