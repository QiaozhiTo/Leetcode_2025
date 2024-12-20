class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_count = {}
        for char in s:
            s_count[char] = s_count.get(char, 0) + 1
        for char in t:
            if char in s_count:
                s_count[char] -= 1
        for val in s_count.values():
            if val != 0:
                return False
        return True
    