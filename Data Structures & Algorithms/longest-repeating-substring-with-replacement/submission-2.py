class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        max_len=0
        n=len(s)
        for i in range(n):
            freq={}
            for j in range(i,n):
                freq[s[j]]=freq.get(s[j],0)+1
                max_freq=max(freq.values())
                window_len=j-i+1
                if window_len-max_freq<=k:
                    max_len=max(max_len,window_len)
                else:
                    freq[s[j]]=freq.get(s[j],0)-1
        return max_len

            
        


        
        