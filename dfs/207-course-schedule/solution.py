class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        
        hm = defaultdict(list) # course taken -> courses unlocked[]
        indegree = [0] * numCourses

        for course, prereq in prerequisites:
            indegree[course] += 1
            hm[prereq].append(course)

        q = deque([i for i, inde in enumerate(indegree) if inde == 0])
        numTaken = 0

        while q:
            taking = q.popleft()
            numTaken += 1

            for unlocked in hm[taking]:
                indegree[unlocked] -= 1
                if indegree[unlocked] == 0:
                    q.append(unlocked)

        return numCourses == numTaken  