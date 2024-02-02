import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())

graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, -1, -1, 0, 1, 0, 1, 1]
dy = [-1, 0, 1, 1, 1, -1, 0, -1]

q= deque()

for i in range(n):
    for j in range(m):
        if graph[i][j] ==1:
            q.append([i,j])

answer = -1
def bfs():
    global answer
    while q:
        x,y = q.popleft()
        for k in range(8):
            nx=dx[k]+x
            ny=dy[k]+y
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny] !=0:
                continue
            q.append([nx,ny])
            graph[nx][ny] = graph[x][y] +1
            answer = max(answer, graph[nx][ny])
    print(answer-1)
            


bfs()