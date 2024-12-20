# class Solution:
#     def isAnagram(self, s: str, t: str) -> bool:
#         if len(s) != len(t):
#             return False
        
#         s_count = {}
        
#         for char in s:
#             s_count[char] = s_count.get(char, 0) + 1
#         for char in t:
#             if char in s_count:
#                 s_count[char] -= 1
#         for val in s_count.values():
#             if val != 0:
#                 return False
#         return True
    
    
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s, count_t = {}, {}
        for i in range(len(s)):
            count_s[s[i]] = count_s.get(s[i], 0) + 1
            count_t[t[i]] = count_t.get(t[i], 0) + 1
        return count_t == count_s
            
            
            
        
    