class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = {}
        a = 0
        count = 0
        for i in range(len(s)):
            l[s[i]] = i
            if s[i] not in l:
                 count = max(count, i-a+1)
            else:
                if l[s[i]] < a:
                    count = max(count, i-a+1)
                else:
                    a = l[s[i]] + 1
            return count





