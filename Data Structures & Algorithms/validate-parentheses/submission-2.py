class Solution:
    def isValid(self, s: str) -> bool:
        mp={
            "]":"[",
            ")":"(",
            "}":"{"
        }
        stack=[]
        for ch in s:
            if ch not in mp:
                stack.append(ch)
            else:
                if not stack:
                    return False

                elif stack[-1]==mp[ch]:
                    stack.pop()
                else:
                    return False
        return len(stack)==0

        