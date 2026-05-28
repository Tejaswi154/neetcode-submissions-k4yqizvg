class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        else:
            p=sorted(s)
            q=sorted(t)
            for i in range(len(p)):
                if p[i]!=q[i]:
                    return False
        return True
        