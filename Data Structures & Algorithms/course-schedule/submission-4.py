class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        graph={i:[] for i in range(numCourses)}
        for prereq in prerequisites:
            graph[prereq[0]].append(prereq[1])  
        visitset=set()
        def dfs(crs):
            if crs in visitset:
                return False
            if graph[crs] ==[]:
                return True
            
            visitset.add(crs)
            for preqs in graph[crs]:
                if not dfs(preqs):
                    return False
            visitset.remove(crs)
            return True
        for i in range(numCourses):
            if not dfs(i) : return False
        return True
        
            

        