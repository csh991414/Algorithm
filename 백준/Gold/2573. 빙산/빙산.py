import sys
from collections import deque
input = sys.stdin.readline

def bfs(a, b):
    visited[a][b] = 1
    q = deque()
    q.append((a, b))

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                if graph[nx][ny] != 0:
                    visited[nx][ny] = 1
                    q.append((nx, ny))
                else:
                    cnt[x][y] += 1
    return 1

n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

ycnt = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

while 1:
    answer = []
    visited = [[0] * m for _ in range(n)]
    cnt = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and not visited[i][j]:
                answer.append(bfs(i, j))

    for i in range(n):
        for j in range(m):
            graph[i][j] -= cnt[i][j]
            if graph[i][j] < 0:
                graph[i][j] = 0

    if len(answer) == 0 or len(answer) >= 2:
        break
    ycnt += 1
if len(answer) >= 2:
    print(ycnt)
else:
    print(0)

