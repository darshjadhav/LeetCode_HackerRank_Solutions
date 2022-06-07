# LEETCODE 11: Container With Most Water Two Pointer Solution
# Time: O(n)
# Space: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1

        volMax = 0

        while l<r:
            tempval = min(height[l], height[r]) * (r-l)
            volMax = max(tempval, volMax)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return volMax
