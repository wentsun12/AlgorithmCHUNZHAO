# 78 subsets
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results =[[]] 
        for num in nums:
            new_ones = []
            for result in results:
                new_one = result + [num]
                new_ones.append(new_one)
                
            results.extend(new_ones)
            
        return results
