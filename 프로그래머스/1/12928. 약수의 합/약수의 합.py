def solution(n):
    answer = []
    
    for i in range(1,int(n**(1/2)) + 1):
        if n% i ==0:
            answer.append(i)
            if i   <  n //i:
                answer.append(n//i)
                
    print(answer)
            
        
    
    return sum(answer)