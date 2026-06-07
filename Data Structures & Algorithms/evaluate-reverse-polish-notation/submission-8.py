class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        arr=tokens[:]
        while len(arr)>1:
            for i in range(len(arr)):
                if arr[i] in "*/+-":
                    a=int(arr[i-2])
                    b=int(arr[i-1])
                    if arr[i]=='+':
                        res=a+b
                    elif arr[i]=='-':
                        res=a-b
                    elif arr[i]=='*':
                        res=a*b
                    else:
                        res=int(a/b)
                    arr=arr[:i-2]+[str(res)]+arr[i+1:]
                    break
        return int(arr[0])

                
        