def solution(s):
    answer = 0
    
    while s:
        x = s[0]
        count_x = 0
        count_other = 0
        i = 0
        
        for i in range(len(s)):
            if s[i] == x:
                count_x += 1
            else:
                count_other += 1
            
            if count_x == count_other:
                break
        
        s = s[i+1:]
        answer += 1
        
    return answer