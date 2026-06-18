class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        min_len=float('inf')
        res=""
        need={}
        
        
        for ch in t:
            need[ch]=need.get(ch,0)+1
        need_count=len(need)
        have=0

        l=0
        window={}
        res=[-1,-1]
        for r in range(len(s)):
            window[s[r]]=window.get(s[r],0)+1
            if s[r] in need and window[s[r]]==need[s[r]]:
                have+=1

            while have==need_count:
                if r-l+1<min_len:
                    min_len=r-l+1
                    res=[l,r]
                window[s[l]]-=1
                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -= 1
                l+=1
            
        l,r=res
        return s[l:r+1] if min_len!=float('inf') else ""
                    
                    


        