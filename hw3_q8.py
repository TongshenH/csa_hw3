class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a = {}
        for i in s:
            if i not in a:
                a[i] = 1
            else:
                a[i] += 1
        for l in t:
            if l in a:
                a[l] -= 1
            else:
                return False
        for val in a.values():
            if val != 0:
                return False
            else:
                return True
