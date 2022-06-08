# LEETCODE 20: Using Stack to check if parentheses are valid in string
# Time: O(n)
# Space: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # Stack to keep track of opening parentheses
        pDict = {")": "(","]": "[","}": "{"} # Hashmap to keep track of mappings

        for c in s:
            # If Character is a closing brackett
            if c in pDict:
                # If stack contains parentheses and top of stack consists of correct opening parentheses, remove opening parentheses
                if stack and stack[-1] == pDict[c]:
                    stack.pop()
                else:
                    return False # If elem doesn't match return False
            else:
                stack.append(c)

        return True if not stack else False
