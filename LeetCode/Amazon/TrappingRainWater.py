# Time: O(n) Space: O(1)
class Solution:
    def trap(self, height: List[int]) -> int:
        # min(l,r) - h[i] = x (>=0)
        if not height:
            return 0

        l, r = 0, len(height)-1
        lMax, rMax = height[l], height[r]
        res = 0
        while l < r:
            if lMax < rMax:
                l += 1
                lMax = max(lMax, height[l])
                tempv = lMax - height[l]
                res += lMax - height[l]
            else:
                r -= 1
                rMax = max(rMax, height[r])
                tempv = rMax - height[r]
                res += rMax - height[r]

        return res
