class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = {}
        nums = sorted(nums)
        for i in range(len(nums)):
            target = -1 * nums[i]
            l = i+1
            r = len(nums) - 1
            while l < r:
                curr = nums[l] + nums[r]
                if curr == target:
                    res[(nums[i],nums[l],nums[r])] = [nums[i],nums[l],nums[r]]
                    l+=1
                    r-=1
                elif curr < target:
                    l += 1
                else:
                    r -= 1
        return list(res.values())
