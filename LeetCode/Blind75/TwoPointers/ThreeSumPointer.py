# LEETCODE 15: Pointer Solution (using Quick Sort)
# Time: O(n^2)
# Space: O(1) or O(n)
# Sorting arrays is time: O(nlogn)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for ind, val in enumerate(nums):
            # Skip duplicates
            if ind > 0 and val == nums[ind - 1]:
                continue

            l, r = ind + 1, len(nums) - 1

            while l < r:
                threeSum = val + nums[l] + nums[r]

                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([val, nums[l], nums[r]])
                    l += 1
                    # Increment Left Pointer if the two values are the same
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return res
