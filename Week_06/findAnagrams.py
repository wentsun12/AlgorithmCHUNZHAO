class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hash = {}   
        for c in p:
            if c in hash:
                hash[c] += 1
            else:
                hash[c] = 1
        count = len(p) 
        
        result = []
        left = 0   
        right = 0
        while right < len(s):
            if s[right] in hash:
                hash[s[right]] -= 1
                if hash[s[right]] >= 0:
                    count -= 1
            if count == 0:
                result.append(left)
            
            if right == left + len(p) - 1:   
                if s[left] in hash:    
                    if hash[s[left]]>=0:  
                        count += 1
                    hash[s[left]] += 1
                left += 1
            right += 1
            
        return result
