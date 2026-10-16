class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Idea 
        # any string is ever gonna contain letter's among a-z
        # so take the character count array 
        count_tracker = {}

        for string in strs:
            count = [0]*26
            # for each string we count the characters in the count array
            for char in string :
                count[ord(char) - ord('a')] += 1

            # the key shouldn't change it is the constant we use to find similar elements so used tuple
            key = tuple(count)
            # if the key is not present in the hashmap add only the key
            if key not in count_tracker:
                count_tracker[key] = []
            # add the current string to it's corresponding key
            count_tracker[key].append(string)
        # return the output array
        return list(count_tracker.values())
            