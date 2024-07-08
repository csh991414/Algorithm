from collections import deque
def solution(n, m, section):
    answer = 0
    
    q = deque(section)
    
    while q:
        current_start = q.popleft()
        
        while q and q[0] < current_start + m:
            q.popleft()
        
        answer += 1  
    
    return answer