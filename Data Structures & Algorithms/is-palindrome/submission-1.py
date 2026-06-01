class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars=[]
        for ch in s:
            if ch.isalnum():
                chars.append(ch.lower())
        clean="".join(chars)
        return clean==clean[::-1]

        
        
        
        