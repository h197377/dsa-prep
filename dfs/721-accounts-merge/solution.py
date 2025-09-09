class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        email_to_name = {} # email -> name
        graph = defaultdict(set)

        for account in accounts:
            name, emails = account[0], account[1:]

            for email in emails:
                email_to_name[email] = name

            for i in range(len(emails)):
                graph[emails[0]].add(emails[i])
                graph[emails[i]].add(emails[0])

        visited = set()
        res = []

        def dfs(email, grouping):
            if email not in visited:
                grouping.append(email)
                visited.add(email)
                for nei in graph[email]:
                    if nei not in visited:
                        dfs(nei, grouping)

        for email in email_to_name:
            if email not in visited:
                grouping = []
                dfs(email, grouping)
                res.append([email_to_name[email]] + (sorted(grouping)))

        return res