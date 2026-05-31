class Solution:

    def encode(self, strs: List[str]) -> str:
        ls=[]
        final=""
        for word in strs:
            final+=str(len(word))+'#'+word
        return final

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
            

        
