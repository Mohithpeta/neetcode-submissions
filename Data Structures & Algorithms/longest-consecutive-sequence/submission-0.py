class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        nums = sorted(nums)
        i = 0
        j = 1
        longest = 1
        cur_longest = 1

        while j < len(nums):
            if nums[j] - nums[i] == 1:
                cur_longest += 1
                i = j
            elif nums[j] == nums[i]:
                pass
            else:
                # reset when the sequence breaks
                cur_longest = 1
                # initialize the current jth element for i
                i = j

            longest = max(longest, cur_longest)
            j += 1

        return longest