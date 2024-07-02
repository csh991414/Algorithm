def solution(ab, signs):
    answer = 0
    for i in range(len(ab)):
        if signs[i] == False:
            answer += ab[i] * -1
        else:
            answer += ab[i]
    
    return answer