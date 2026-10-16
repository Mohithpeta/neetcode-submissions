class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        # we have the count hashmap
        # extract top k counts from the hashmap
        # Sort by value (descending)
        rev_sorted_count = sorted(count, key=count.get, reverse=True)
        return rev_sorted_count[:k]   