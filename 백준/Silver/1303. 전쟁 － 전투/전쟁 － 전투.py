import sys
from collections import deque
#input = sys.stdin.readline()

n,m = map(int,input().split())

graph = []

for i in range(m):
    graph.append(list(input()))

visited = [ [0] *n for _ in range(m)]

wcount=0
bcount=0


dx = [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(x,y,color):
    count=0
    q=deque()
    q.append((x,y))
    visited[x][y] = 1

    while q:
        x,y= q.popleft()

    
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <=nx and  nx<m and 0<=ny and ny <n:
                if graph[nx][ny] == color and not visited[nx][ny]:
                    visited[nx][ny] =1
                    q.append((nx,ny))
                    count+=1

    return count +1


for i in range(m):
    for j in range(n):
        if graph[i][j] == 'W' and not visited[i][j]:
            wcount += bfs(i,j,'W') **2
        elif graph[i][j] == 'B' and not visited[i][j]:
            bcount+= bfs(i,j,'B')**2

print(wcount,bcount)



