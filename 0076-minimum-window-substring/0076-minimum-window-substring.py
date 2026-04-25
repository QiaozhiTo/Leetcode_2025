class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window, count = {},{}
        for c in t:
            count[c] = count.get(c, 0) + 1
        have, need = 0, len(count)
        res, resLen = [-1, -1], float('inf')

        l = 0
        for r in range(len(s)):
            window[s[r]] = 1 + window.get(s[r], 0)
            if s[r] in count and count[s[r]] == window[s[r]]:
                have += 1

            while have == need:
                if r - l + 1 < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -= 1
                if s[l] in count and count[s[l]] > window[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return "" if resLen == float('inf') else s[l : r + 1]