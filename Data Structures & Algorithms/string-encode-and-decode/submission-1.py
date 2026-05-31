class Solution:

    def encode(self, strs: List[str]) -> str:
        parts=[]
        final=""
        for word in strs:
            parts.append(str(len(word))+'#'+word)
        return "".join(parts)

    def decode(self, s: str) -> List[str]:
        ls=[]
        i=0
        while(i<len(s)):
        
            j=i
            while(s[j]!='#'):
                j+=1
            length=int(s[i:j])
            word=str(s[j+1:j+length+1])

            ls.append(word)
            i=j+1+length
        return ls
            

        
