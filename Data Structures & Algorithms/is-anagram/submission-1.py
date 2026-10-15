class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counter = [0]*26 
        for a,b in zip(s,t):
            counter[ord(a) - ord('a')] += 1
            counter[ord(b) - ord('a')] -= 1
        
        for num in counter:
            if num != 0:
                return False
        return True