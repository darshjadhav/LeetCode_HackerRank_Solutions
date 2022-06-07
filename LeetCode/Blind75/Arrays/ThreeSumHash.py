# LEETCODE 15: LEETCODE Hash Table Solution (No Sorting)
# Time: O(n^2)
# Space: O(n)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res, dups = set(), set()
        seen = {}
        for i, valOne in enumerate(nums):
            if valOne not in dups:
                dups.add(valOne)
                for j, valTwo in enumerate(nums[i+1:]):
                    comp = -valOne - valTwo
                    if comp in seen and seen[comp] == i:
                        res.add(tuple(sorted((valOne, valTwo, comp))))
                    seen[valTwo] = i
        return res
