# https://leetcode.com/problems/make-the-string-great/
class Solution:
    def makeGood(self, s: str) -> str:
        stack = []
        for c in list(s):
            if stack and abs(ord(c) - ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)