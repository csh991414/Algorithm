def solution(answers):
    answer = []
    m = -999
    
    st_score = [0,0,0]
    st_1 = [1,2,3,4,5]
    st_2 = [2,1,2,3,2,4,2,5]
    st_3 = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)):
        if answers[i] == st_1[i % len(st_1)]:
            st_score[0] +=1
            
        if answers[i] == st_2[i % len(st_2)]:
            st_score[1] +=1
        
        if answers[i] == st_3[i % len(st_3)]:
            st_score[2] +=1
    
    for i in range(3):
        if max(st_score) == st_score[i]:
            answer.append(i+1)
    
    
    
    return answer