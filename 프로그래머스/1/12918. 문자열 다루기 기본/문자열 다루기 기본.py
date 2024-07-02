def solution(s):
    answer = True
    if len(s) != 4 and len(s) != 6:
        return False
    
    li = list(s)
    for i in li:
        if i.isdigit():
            continue
        else:
            return False
    
    return answer