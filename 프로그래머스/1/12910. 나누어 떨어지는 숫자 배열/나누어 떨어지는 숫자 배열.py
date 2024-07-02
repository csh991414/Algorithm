def solution(arr, divisor):
    answer = []
    for i in arr:
        if int(i) % divisor ==0:
            answer.append(i)
    
    answer.sort()
    if len(answer) >0:
        return answer
    else:
        return [-1]