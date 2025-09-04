class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        res = []
        
        for key in count:
            if count[key] > len(nums) / 3:
                res.append(key)
        return res