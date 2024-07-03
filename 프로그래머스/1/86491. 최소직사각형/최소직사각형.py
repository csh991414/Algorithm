def solution(sizes):
    answer = 0
    m1= -999
    m2 = -999
    for i in range(len(sizes)):
        
        if sizes[i][0] < sizes[i][1]:
            sizes[i][0],sizes[i][1] = sizes[i][1],sizes[i][0]
            
        if sizes[i][0] > m1:
            m1 = sizes[i][0]    
        if sizes[i][1] > m2:
            m2 = sizes[i][1]
            
            
    answer = m1 * m2
    
    
    return answer