class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen={}
        max_length=0
        l=0
        for r in range(len(s)):
            if s[r] in last_seen:
                l=max(l,last_seen[s[r]]+1)
            last_seen[s[r]]=r
            max_length=max(max_length,r-l+1)
            
        return max_length
            
            
                
                    


        