class Solution:
    def longestPalindrome(self, s: str) -> str:
        largestsub = ""
        for i in range(len(s)):
            odd = self.longestsubindex(s,i,i)
            even = self.longestsubindex(s,i,i+1)
            larger = odd if len(odd)>len(even) else even
            largestsub = largestsub if len(largestsub) > len(larger) else larger
        
        return largestsub
    
    def longestsubindex(self,s,left,right):
        leftindex = 0
        rightindex = 0 
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                leftindex = left
                rightindex = right
            else:
                break
            
            left-=1
            right+=1
        return s[leftindex:rightindex+1]
