# LEETCODE 217
# Time: O(n)
# Space: O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) < len(nums):
            return True
        else:
            return False
