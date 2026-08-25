class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # for every new number (nums[i]) where nums[i] - 1 is not in the list, keep track of all elts (nums[j]) w/ i < j
        # return number with the largest 

        num_set = set(nums)
        res = 0
        for n in nums:
            curr_len = 0
            if (n-1) not in num_set:
                curr_len += 1
                while (n+curr_len) in num_set:
                    curr_len += 1
            res = max(res, curr_len)
        return res