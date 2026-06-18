class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m=len(s1)
        n=len(s2)
        if m>n:
            return False
        freq1=[0]*26
        window=[0]*26
        for ch in s1:
            freq1[ord(ch)-ord('a')]+=1
        for i in range(m):
            window[ord(s2[i])-ord('a')]+=1
        if freq1==window:
            return True
        for r in range(m,n):
            window[ord(s2[r])-ord('a')]+=1
            window[ord(s2[r-m])-ord('a')]-=1
            
            if freq1==window:
                return True
            
            
        return False