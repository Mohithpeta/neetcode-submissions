class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Hash map approach

        seen = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seen:
                return [seen[complement],i]
            seen[nums[i]] = i
        