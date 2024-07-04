def solution(strings, n):
    answer = []
    answer = sorted(strings,key= lambda string:string[n])
    
    for i in range(len(strings)):
        for j in range(len(strings)):
            if answer[i][n] == answer[j][n]:
                if answer[i] < answer[j]:
                    answer[i],answer[j] = answer[j],answer[i]
                    
    
    
        
    
    
    return answer