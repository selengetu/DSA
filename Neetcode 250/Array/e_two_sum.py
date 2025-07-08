class Solution(object):
    def twoSum(self, nums, target):

        seen = {}
        for i, num in enumerate(nums):
            diff = target-num
            if diff in seen:
                return i, seen[diff]
            else:
                seen[num] = i