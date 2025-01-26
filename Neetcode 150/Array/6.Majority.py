class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for i in range(len(nums)):
               count[nums[i]] = 1 + count.get(nums[i], 0)
        keymax = max(zip(count.values(), count.keys()))[1]
        return keymax
    

    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        res= max_count = 0
        for i in nums:
               count[i] = 1 + count.get(i, 0)
               if count[i] > max_count:
                res = i
                max_count = count[i]
        return res
    
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]

class Solution:
    def majorityElement(self, nums):
        res = count = 0

        for num in nums:
            if count == 0:
                res = num
            count += (1 if num == res else -1)
        return res