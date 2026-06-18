class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_len=float('inf')
        res=""
        need={}
        n=len(s)
        for ch in t:
            need[ch]=need.get(ch,0)+1
        for i in range(len(s)):
            window={}
            for j in range(i,n):
                window[s[j]]=window.get(s[j],0)+1
                valid=True
                for ch in need:
                    if window.get(ch,0)<need[ch]:
                        valid=False
                        break
                if valid:
                    if j-i+1<min_len:
                        min_len=j-i+1
                        res=s[i:j+1]
        return res
                    
                    


        