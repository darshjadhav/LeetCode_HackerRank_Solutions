# TIME: O(n) SPACE: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(0, len(nums)):
            tempnum = target - nums[i]
            if tempnum in hashmap:
                return [i, hashmap[tempnum]]
            else:
                hashmap[nums[i]] = i
