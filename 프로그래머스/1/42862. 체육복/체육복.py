def solution(n, lost, reserve):
    answer = 0
    
    student = [1] * (n)
    
    for i in lost:
        student[i-1] -=1
    for i in reserve:
        student[i-1] +=1
    print(student)
    
    for i in range(n):
        if i >0:
            if i == n-1:
                if student[-1] ==0:
                    if student[-2] ==2:
                        student[-1] +=1
                        student[-2] -=1
            else:
                if student[i] ==0:
                    if student[i-1] ==2:
                        student[i] +=1
                        student[i-1] -=1
                    elif student[i+1] ==2:
                        student[i] +=1
                        student[i+1] -=1
                        
            
            
        else:
            if student[i] ==0:
                if student[i+1] ==2:
                    student[i] +=1
                    student[i+1] -=1
    
    
        #print(student)
    for i in student:
        if i >0:
            answer+=1
    
    
    return answer