def solution(ph):
    answer = ''
    for i in range (len(ph)-4):
        answer+= '*'
    for i in range(4,0,-1):
        answer += ph[-i]
    return answer