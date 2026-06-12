class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph={ i:[] for i in range(n)}
        for start,end in edges:
            graph[start].append(end)
            graph[end].append(start)
        visited=set()
        def dfs(node,parent):
            visited.add(node)
            for neighbor in graph[node]:
                if parent ==neighbor:
                    continue
                if neighbor in visited:
                    return False
                if not dfs(neighbor,node):
                    return False
            return True
        if not dfs(0,-1):
            return False
        return len(visited)==n
        

            


        