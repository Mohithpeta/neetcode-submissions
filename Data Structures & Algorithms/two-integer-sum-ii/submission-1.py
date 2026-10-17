class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        i = 0
        j = len(nums)-1
        while i<j:
            if nums[i]+nums[j] == target:
                return [i+1,j+1]
            elif nums[i]+nums[j] > target:
                j-=1
            elif nums[i]+nums[j] < target:
                i+=1
        return False