def solution(age):
    answer = ''
    li = list(str(age))
    for i in range (len(li)):
        answer += chr(ord('a')+ int(li[i]))
        
    
    return answer