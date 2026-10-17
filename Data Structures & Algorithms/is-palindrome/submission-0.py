class Solution:
    def isPalindrome(self, s: str) -> bool:

        store = ""            
        for char in s:
            if char.isalnum():
                store += char.lower()
        length_new = len(store)
        flag = True
        i = 0
        j = len(store)-1
        while i <= j:
            if store[i] == store[j] :
                i += 1
                j -= 1
            elif store[i] != store[j] and i != j:
                return False
            elif i == j :
                flag = True
        return flag
                    