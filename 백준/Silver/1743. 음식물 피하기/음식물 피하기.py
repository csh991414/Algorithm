import sys
from collections import deque
input = sys.stdin.readline


n,m,k = map(int,input().split())
graph = [ [0] *m for _ in range(n)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]


for i in range(k):
    a,b = map(int,input().split())
    graph[a-1][b-1] = 1

def bfs(x,y):

    q= deque()
    q.append((x,y))
    graph[x][y] =0
    cnt =0
    
    while q:
        a,b = q.popleft()
        cnt+=1
        for i in range(4):
            nx = dx[i] + a
            ny = dy[i] + b

            if 0<= nx < n and 0<= ny < m and graph[nx][ny] ==1:
                q.append((nx,ny))
                graph[nx][ny] = 0
                


    
    return cnt


max_count =0
for i in range(n):
    for j in range(m):
        if graph[i][j] ==1:
            max_count = max(max_count,bfs(i,j))

print(max_count)
