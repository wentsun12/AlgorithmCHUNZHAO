import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums, k):
        res = []
        dic = Counter(nums)
        max_heap = [(-val, key) for key, val in dic.items()] #heapq中生成的小顶堆，所以用-val
        heapq.heapify(max_heap)
        for i in range(k):
            res.append(heapq.heappop(max_heap)[1])
        return res   
