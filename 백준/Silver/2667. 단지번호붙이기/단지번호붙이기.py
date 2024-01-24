import sys
from collections import deque

n=int(input())

graph= []
result = []
count=0

for _ in range(n):
    graph.append(list(map(int,input().rstrip())))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(a,b):
    global count
    if a <0 or a>=n or b<0 or b>= n:
        return

    if graph[a][b] == 1:
        count+=1
        
        graph[a][b]=0

        for i in range(4):
            nx = a+dx[i]
            ny = b+dy[i]
            dfs(nx,ny)






for i in range(n):
    for j in range(n):
        if graph[i][j]==1:
            dfs(i,j)
            result.append(count)
            count=0

result.sort()
print(len(result))
for i in result:
    print(i)
            
