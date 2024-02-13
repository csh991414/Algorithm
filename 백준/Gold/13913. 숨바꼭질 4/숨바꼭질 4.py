import sys
from collections import deque
input = sys.stdin.readline

n,k= map(int,input().split())

maxnum= 100001
graph = [0] * maxnum # 횟수를 입력받음
check = [0] * maxnum # 이전에 어디서 왔는지를 입력받음


def past(now):
    t=now
    data=[]
 
    for _ in range(graph[t] + 1):#횟수만큼 맨끝에서 과거로 돌아가면서 출력
        data.append(t)
        t = check[t]
    print(' '.join(map(str,data[::-1])))

    


def bfs():
    q= deque()
    q.append(n)

    while q:
        x = q.popleft()

        if x ==k:
            print(graph[x])
            past(x)
            return

        for i in (x+1,x-1,x*2):
            if 0<=i<maxnum and graph[i] ==0:
                graph[i] = graph[x]+1
                q.append(i)
                check[i] = x

bfs()
