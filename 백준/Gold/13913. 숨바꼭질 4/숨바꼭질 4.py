import sys
input = sys.stdin.readline
from collections import deque

max_num = 100000
visited = [0] *(max_num +1)
n,k = map(int,input().split())
check = [0] *(max_num + 1)

def past(now):
    data = []
    k= now

    for _ in range(visited[k] + 1):
        data.append(k)
        k = check[k]

    print(' '.join(map(str,data[::-1])))





def bfs():
    q= deque()
    q.append(n)

    while q:
        x= q.popleft()
        if x == k:
            print(visited[x])
            past(x)
            return

        for i in (x+1,x-1,x*2):
            if 0<= i <= max_num and visited[i] ==0:
                    visited[i] = visited[x]+1
                    q.append(i)
                    check[i] = x

bfs()
