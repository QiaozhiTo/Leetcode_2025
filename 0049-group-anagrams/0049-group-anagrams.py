# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#         res = defaultdict(list)
#         for string in strs:
#             count = [0] * 26
#             for c in string:
#                 count[ord('a') - ord(c)] += 1
#             res[tuple(count)].append(string)
#         return list(res.values())
    
# lists are mutable and cannot be used as keys in a dictionary, whereas tuples are immutable and can be used as keys.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)
        return list(res.values())
        