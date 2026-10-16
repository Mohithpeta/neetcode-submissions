import re

class Solution:

    def encode(self, strs: list[str]) -> str:
        encoded_string = ""
        for i in range(len(strs)):
            encoded_string += strs[i]+"?!"
        return encoded_string
    def decode(self, s: str) -> list[str]:
        result = re.split(r'\?!', s)
        return result[:-1]