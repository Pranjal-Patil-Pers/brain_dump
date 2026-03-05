class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}
        max_len = 0
        l,r = 0,0
        for r in range(len(s)):
            char=s[r]
            if char in char_map and char_map[char]>=l:
                l=char_map[char]+1
            char_map[char]=r
            max_len=max(r-l+1,max_len)
        return max_len