class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        start = 0
        max_char_count = 0
        max_length = 0
        
        for end in range(len(s)):
            count[s[end]] = count.get(s[end], 0) + 1

            max_char_count = max(max_char_count, count[s[end]])

            while (end - start + 1) - max_char_count > k:
                count[s[start]] -= 1
                start += 1

            max_length = max(max_length, end - start + 1)

        return max_length