class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pres = [1] * len(nums)
        pres[1] = nums[0]
        for i in range(2,len(nums)):
            pres[i] = nums[i-1] * pres[i-1]

        suffs = [1] * len(nums)
        suffs[len(nums) - 2] = nums[-1]
        for i in range(len(nums) - 2, -1, -1):
            # print(suffs)
            suffs[i] = nums[i+1] * suffs[i+1]
        res = [0] * len(nums)

        for i in range(len(nums)):
            res[i] = pres[i] * suffs[i]
        return res