def solution(n):
    answer = 0
    li = list(map(str,list(str(n))))
    li.sort(reverse= True)
    answer  = int(''.join(li))
    return answer