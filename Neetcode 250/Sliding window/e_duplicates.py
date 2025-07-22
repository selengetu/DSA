class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()

        l = 0
        for r in range(len(s)):
            if r-l > k:
                window.remove(nums[l])
                l+1=1
            if num[r] in window:
                return True
            window.add(num[r])