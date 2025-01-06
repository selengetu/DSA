from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Initialize an empty set to track seen numbers
        seen = set()

        # Loop through the array
        for num in nums:
            # If the number is already in the set, we found a duplicate
            if num in seen:
                return True
            # Otherwise, add the number to the set
            seen.add(num)

        # If no duplicates are found, return False
        return False
