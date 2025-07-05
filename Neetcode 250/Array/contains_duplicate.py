from typing import List

class Solution:
      def hasDuplicate(self, nums: List[int]) -> bool:

        seen = set()
        for i in nums:
            if i in seen:
                return True
            else:
                seen.add(i)
        return False