class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            return Counter(s) == Counter(t)
        else:
            return False