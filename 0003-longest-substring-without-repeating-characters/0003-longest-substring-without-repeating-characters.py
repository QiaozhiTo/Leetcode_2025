class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        cur_len = 0
        count = {}
        for i in range(len(s)):
            count[s[i]] = count.get(s[i], 0) + 1
            while count[s[i]] > 1:
                count[s[cur_len]] -= 1
                cur_len += 1
            res = max(res, i-cur_len+1)
        return res
                
                
                
            
        