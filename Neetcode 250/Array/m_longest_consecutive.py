class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            prev = num-1
            if prev not in numSet:
                length = 1
                while (num + length) in numSet:
                    length +=1
                longest = max(length, longest)
        return longest