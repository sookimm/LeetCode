class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            s = s.lower()
            t = t.lower()
            return sorted(s) == sorted(t)
        else:
            return False
        