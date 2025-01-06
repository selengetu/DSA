class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * (2 * n)  # Create a new list of size 2n
        for i, num in enumerate(nums):
            result[i] = num         # Copy the first part
            result[i + n] = num     # Copy the second part
        return result