class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        mp={}
        for word in strs:
            #freq_count:
            freq={}
            for ch in word:
                freq[ch]=freq.get(ch,0)+1
            #create key:
            key=""
            for ch in sorted(word):
                key+=ch+str(freq[ch])
            if key not in mp:
                mp[key]=[]
            mp[key].append(word)
        return list(mp.values())
        
        
            

        