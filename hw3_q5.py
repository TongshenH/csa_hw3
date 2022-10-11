class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        d = {'(': ')', '{': '}', '[': ']'}
        a = []
        for i in s:
            if i in d.key():
                a.append(i)
            elif len(a) == 0 or d[a.pop(-1)] != i:
                return False
        return True