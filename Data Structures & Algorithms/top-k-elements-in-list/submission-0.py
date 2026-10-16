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
        result = []
        while k > 0:
            max_key = max(count, key=count.get)   
            result.append(max_key)
            del(count[max_key])
            k -= 1
        return result