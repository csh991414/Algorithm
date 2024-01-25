import sys
from collections import deque
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
n,m,k = map(int,input().split())

graph = [[0] * (m) for _ in range (n)]

for i in range(k):
    a,b= map(int,input().split())
    graph[a-1][b-1] = 1
    
count =0
arr=[]
dx = [0,0,1,-1]
dy = [1,-1,0,0]


def dfs(x,y):
    global count
    if x<0  or y<0 or x>=n or y>=m:
        return False

    if graph[x][y] ==1:
        graph[x][y]=0
        count+=1
        for i in range(4):
            nx= x+dx[i]
            ny= y+dy[i]
            dfs(nx,ny)
        return True
    return False

for i in range(n):
  for j in range(m):
    if dfs(i, j) == True:
      arr.append(count)
      count = 0    

print(max(arr))
