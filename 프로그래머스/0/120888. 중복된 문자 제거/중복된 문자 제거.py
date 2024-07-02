def solution(mys):
    answer = ''
    there = []
    
    m = list(mys)
    for i in range (len(m)):
        if m[i] not in there:
            there.append(m[i])
    answer = ''.join(there)    
    
    
    return answer