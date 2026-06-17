class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m=len(s1)
        freq1=[0]*26
        for ch in s1:
            freq1[ord(ch)-ord('a')]+=1
        for i in range(len(s2)-m+1):
            freq2=[0]*26
            for j in range(i,i+m):
                freq2[ord(s2[j])-ord('a')]+=1
            if freq1==freq2:
                return True
        return False