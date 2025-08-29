class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def getDist(x, y):
            return math.sqrt((x ** 2) + (y ** 2))
        
        if not points or k < 0:
            return []
        
        h = []
        heapq.heapify(h)
        for p in points:
            heapq.heappush(h, (-getDist(p[0], p[1]), [p[0], p[1]] ))
            if len(h) > k:
                heapq.heappop(h)
        
        return [point for _, point in h]
        