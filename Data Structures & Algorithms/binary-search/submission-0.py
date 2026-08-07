class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            c = (l+r) // 2
            print(c)
            if nums[c] == target:
                return c
            elif nums[c] < target:
                l = c + 1
            elif nums[c] > target:
                r = c-1
        return -1