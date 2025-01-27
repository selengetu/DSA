class Solution:
    def findLHS(self, nums: List[int]) -> int:
        freq = Counter(nums)  
        max_length = 0

        for key in freq:
            if key + 1 in freq:  # Check if a harmonic pair exists
                max_length = max(max_length, freq[key] + freq[key + 1])

        return max_length