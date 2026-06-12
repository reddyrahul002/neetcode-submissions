class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph={i:[] for i in range(numCourses)}
        for preq in prerequisites:
            graph[preq[0]].append(preq[1])
        
        visited=set()
        visiting=set()
        res=[]
        def dfs(crs):
            if crs in visiting:
                return False
            if crs in visited:
                return True
            visiting.add(crs)
            for preqs in graph[crs]:
               if not dfs(preqs):
                  return False
            visiting.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True
            
        for i in range(numCourses):
            if not dfs(i):
                return []
        return res


            
        