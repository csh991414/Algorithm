def solution(numbers):
    answer = ''
    
    temp = sorted(numbers,key = lambda x: str(x) * 3 , reverse  = True)
    answer = ''.join((map(str,temp)))
    
    if int(answer) != 0:
        return answer
    else:
        return '0'