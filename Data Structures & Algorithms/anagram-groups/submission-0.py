class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mp={}
        for str in strs:
            key=tuple(sorted(str))
            if key not in mp:
                mp[key]=[]
            mp[key].append(str)
        return list(mp.values())
        
        
            

        