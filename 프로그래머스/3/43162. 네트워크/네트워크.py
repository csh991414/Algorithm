
def solution(n, computers):
    visited = [0] *n
    answer =0
    def dfs(v): #2. 맨처음부터 방문처리
        visited[v]=1
        for idx,c in enumerate(computers[v]):
            if c and visited[idx] == 0:
                dfs(idx)# 3. 재귀적으로 처음이랑 연결되어 있으면 연쇄 방문처리
    for pc in range(n):
        if visited[pc] == 0: # 1.방문 안했으면 진행
            dfs(pc)
            answer+=1# 4. 방문할때마다 네트워크 개수 추가
            
    
    
    return answer