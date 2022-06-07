# LEETCODE 125: Is Palindrome Two Pointer Solution
# Time: O(n)
# Space: O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1

            if s[l].lower() != s[r].lower():
                return False

            l += 1
            r -= 1

        return True


# If cannot use isalnum(), use:
# def alphNum(self, c):
#     return (ord("A") <= ord(c) <= ord("Z") or
#             ord("a") <= ord(c) <= ord("z") or
#             ord("0") <= ord(c) <= ord("9"))
