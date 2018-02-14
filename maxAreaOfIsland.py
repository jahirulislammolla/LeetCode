class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        l=len(grid)
        n=len(grid[0])
        visit=[[0 for i in range(n)] for j in range(l)]
        m=0
        for k in range(l):
            for e in range(n):
                if visit[k][e]==0 and grid[k][e]==1:
                    x=[[k,e]]
                    c=1
                    while(len(x)):
                        i,j=x.pop()
                        visit[i][j]=1
                        if i>0 and grid[i-1][j]==1 and visit[i-1][j]==0:
                            x.append([i-1,j])
                            visit[i-1][j]=1
                            c+=1
                        if i<l-1 and grid[i+1][j]==1 and visit[i+1][j]==0:
                            x.append([i+1,j])
                            visit[i+1][j]=1
                            c+=1
                        if j>0 and grid[i][j-1]==1 and visit[i][j-1]==0:
                            x.append([i,j-1])
                            visit[i][j-1]=1
                            c+=1
                        if j<n-1 and grid[i][j+1]==1 and visit[i][j+1]==0:
                            x.append([i,j+1])
                            visit[i][j+1]=1
                            c+=1
                    if c>m:
                        m=c
        return m
   
