def solution(s):
    answer = ''
    s = s.lower()
    li = list(s)
    li.sort()
    answer = ''.join(li)
    return answer
