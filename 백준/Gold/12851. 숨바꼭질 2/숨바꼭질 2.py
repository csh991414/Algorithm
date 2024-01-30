import sys
input = sys.stdin.readline
from collections import deque

max_num = 100000
visited = [0] *(max_num +1)
n,k = map(int,input().split())
times= []

def bfs():
    q= deque()
    q.append(n)


    while q:
        x= q.popleft()

        if x == k:
            times.append(visited[x])
            continue

        for j in (x+1,x-1,x*2):
            if 0<= j <= max_num and (not visited[j] or visited[j] == visited[x]+1):
                q.append(j)
                visited[j] = visited[x] +1
                

    print(min(times))
    print(len(times))

bfs()
