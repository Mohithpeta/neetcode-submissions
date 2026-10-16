class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Idea 
        # any string is ever gonna contain letter's among a-z
        # so take the character count array 
        count_tracker = {}

        for string in strs:
            count = [0]*26
            for char in string :
                count[ord(char) - ord('a')] += 1

            # the key shouldn't change it is the constant we use to find similar elements
            key = tuple(count)
            if key not in count_tracker:
                count_tracker[key] = []
            count_tracker[key].append(string)

        return list(count_tracker.values())
            