def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    j=0
    for i in range((len(score)//m)):
        answer += min(score[j:j+m]) * m
        j = j + m
    
    
    
    
    
    
    return answer