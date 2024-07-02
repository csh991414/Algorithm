def solution(m, num1, num2):
    answer = list(map(str,m))
    answer[num1],answer[num2] = answer[num2],answer[num1]
    answer = ''.join(answer)
    return answer