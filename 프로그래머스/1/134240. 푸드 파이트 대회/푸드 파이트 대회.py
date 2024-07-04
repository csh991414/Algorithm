def solution(food):
    answer = ''
    idx=1
    temp=''
    for i in range(1,len(food)):
        temp += str(i) * (food[i] //2)
        
    answer = temp + ('0' * food[0]) + ''.join(reversed(temp))
    
    
    
    
    
    return answer