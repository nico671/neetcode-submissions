class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h_map = {}
        for i,n in enumerate(nums):
            local_targ = target - n
            if local_targ in h_map:
                return [h_map[local_targ], i]
            else:
                h_map[n] = i
        return []
