from collections import deque
def solution(priorities, location):
    q = deque(priorities)
    answer = 0
    
    while q:
        m = max(q)
        temp = q.popleft()
        location -=1
        if m != temp:
            q.append(temp)
            if location <0:
                location = len(q) - 1
        else:
            answer +=1
            if location <0:
                break
    return answer