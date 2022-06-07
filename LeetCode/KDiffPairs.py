class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:

        uniquenums = set(nums)
        numcounts = Counter(nums)
        counter = 0
        checkset = set()

        if k==0:
            for ind, val in numcounts.items():
                if val >= 2:
                    counter += 1
            return counter


        for elem in uniquenums:
            if elem + k in checkset:
                counter += 1
            if elem - k in checkset:
                counter += 1

            checkset.add(elem)

        return counter
