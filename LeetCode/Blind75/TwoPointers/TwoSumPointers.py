# LEETCODE 167: Two Sum Pointer Solution
# Time: O(n)
# Space: O(1)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1

        while l < r:
            sumval = numbers[l] + numbers[r]

            if sumval == target:
                return [l+1, r+1]

            elif sumval < target:
                l+=1

            else:
                r-=1

        return []
