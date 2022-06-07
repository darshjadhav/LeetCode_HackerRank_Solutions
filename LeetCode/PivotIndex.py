class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        numsum = sum(nums)
        lsum = 0

        for ind, val in enumerate(nums):
            if lsum == (numsum - lsum - val):
                return ind
            lsum += val
        return -1
