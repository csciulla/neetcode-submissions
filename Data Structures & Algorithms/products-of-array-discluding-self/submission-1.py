class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        from functools import reduce
        output = []
        for i in range(len(nums)):
            t = [nums[j] for j in range(len(nums)) if j != i]
            m = reduce(lambda x,y: x*y, t)
            output.append(m)
            t = nums
        return output
