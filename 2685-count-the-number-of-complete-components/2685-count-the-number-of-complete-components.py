from collections import defaultdict

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # Step 1: Build adjacency list
        graph = defaultdict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n
        complete_components = 0

        # DFS to collect all nodes in one connected component
        def dfs(node, component):
            visited[node] = True
            component.append(node)

            for neighbor in graph[node]:
                if not visited[neighbor]:
                    dfs(neighbor, component)

        # Step 2: Traverse every component
        for node in range(n):
            if not visited[node]:
                component = []
                dfs(node, component)

                # Number of vertices in this component
                vertices = len(component)

                # Count edges using degree sum
                degree_sum = 0
                for v in component:
                    degree_sum += len(graph[v])

                actual_edges = degree_sum // 2
                expected_edges = vertices * (vertices - 1) // 2

                if actual_edges == expected_edges:
                    complete_components += 1

        return complete_components