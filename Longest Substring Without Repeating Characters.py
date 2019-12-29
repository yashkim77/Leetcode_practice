def lengthOfLongestSubstring(self, s: str) -> int:
        string = dict()
        start = 0
        maxlen=0
        for end in range(len(s)):
            if s[end] in string:
                start = max(start, string[s[end]]+1)
            string[s[end]]=end
            maxlen = max(maxlen, end-start+1)
        return maxlen
