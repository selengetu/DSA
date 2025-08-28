class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        maxCount = res = 0
        for num in nums:
            count[num] +=1
            if count[num] > maxCount:
                maxCount = count[num]
                res = num
        return res