class Solution:
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        if len(graph)==1:
            return True
        def dfs(s):
            queue=[s]
            y=[]
            while len(queue)>0:
                p=queue.pop()
                visited[p]=True
                for i in graph[p]:
                    visited[i]=True
                    if color[i]==0:
                        if color[p]==1:
                            color[i]=2
                        else:
                            color[i]=1
                        queue.append(i)
                    else:
                        if color[i]==color[p]:
                            return False
            return True            
        p={}
        visited=[]
        for i in range(len(graph)):
            p[i]=0
            visited+=[False]
        m=[]
        for i in range(len(graph)):
            if visited[i]==False:
                color=p
                color[i]=1
                m.append(dfs(i))
        return all(m)    
