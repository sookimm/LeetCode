class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        s_set = set()
        start = 0
        max_length = 0

        for end in range(len(s)):
            while s[end] in s_set:
                s_set.discard(s[start])
                start += 1
            
            s_set.add(s[end])
            max_length = max(max_length, end - start + 1)
            
        return max_length