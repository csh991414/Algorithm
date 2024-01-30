import sys
input = sys.stdin.readline
from collections import deque

max_num = 100000 
n,k = map(int, input().split())
visited = [0] * (max_num +1)

def bfs():
    q= deque()
    q.append(n)

    while q:
        x= q.popleft()
        if x == k:
            print(visited[x])
            break
        for j in (x-1,x+1,x*2):
            if 0<=j<=max_num and not visited[j]:
                visited[j] = visited[x]+1
                q.append(j)




            

bfs()
