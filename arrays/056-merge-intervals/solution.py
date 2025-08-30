class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])

        curr = intervals[0]
        res = []

        for i in intervals:
            if curr[1] >= i[0]:
                curr[0] = min(curr[0], i[0])
                curr[1] = max(curr[1], i[1])
            else:
                # disjoint
                res.append(curr)
                curr = i

        res.append(curr)

        return res