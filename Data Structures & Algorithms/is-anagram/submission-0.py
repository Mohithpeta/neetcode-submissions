class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        S = {}
        T = {}
        for char in s:
            if char in S:
                S[char] += 1
            else:
                S[char] = 1
        for char in t:
            if char in T:
                T[char] += 1
            else:
                T[char] = 1
        if S.items() == T.items() : 
            return True
        return False
