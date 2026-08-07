class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        potential_starts = []
        available = set()
        for n in nums:
            if n - 1 not in nums:
                potential_starts.append(n)
            available.add(n)
        print(potential_starts, available)
        glob_max = 0
        for n in potential_starts:
            curr_count = 1
            while True:
                if n + curr_count in available:
                    print(n + curr_count)
                    curr_count += 1
                else:
                    print(n + curr_count, "else")
                    glob_max = max(curr_count, glob_max)
                    break
        return glob_max