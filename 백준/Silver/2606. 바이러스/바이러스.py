import sys
input = sys.stdin.readline

n= int(input())
m= int(input())

graph = [ [0] * (n+1) for _ in range(n+1)]

visited = [0] * (n+1) 
count =0

for i in range(m):
    a,b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

def dfs(v):
    if visited[v] ==0:
        global count
        visited[v]=1
        count+=1
        for i in range(1, n+1):
            if graph[v][i] == 1 and visited[i] == 0:
                dfs(i)


    else:
        return




dfs(1)
print(count-1)
