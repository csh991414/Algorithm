n= int(input())
m = int(input())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    #양방향그래프라서 둘다 값입력.
    

def DFS(v):
    visited[v] =True
    global count
    count+=1
    for i in graph[v]:
        if not visited[i]:
            DFS(i)

visited = [False for _ in range(n+1)]
count =-1
DFS(1)
print(count)
