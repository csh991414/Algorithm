def solution(rsp):
    answer = ''
    n = list(map(str,list(str(rsp))))
    for i in n:
        if i == '2':
            answer+='0'
        elif i == '0':
            answer += '5'
        else:
            answer += '2'
    return answer