import heapq
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hq = []
        m = Counter(nums)

        for n in m:
            heapq.heappush(hq, (m[n], n))
            if len(hq) > k:
                heapq.heappop(hq)
        
        return [res[1] for res in hq]