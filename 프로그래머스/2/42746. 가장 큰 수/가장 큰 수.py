from itertools import permutations

def solution(numbers):
    answer = ''
    max_val = -1
    
    # numbers 배열의 숫자들을 문자열로 변환한다.
    str_numbers = list(map(str, numbers))
    
    for perm in permutations(str_numbers, len(str_numbers)):
        # 순열을 하나의 문자열로 결합한다.
        tmp = ''.join(perm)
        
        # 현재 생성된 숫자가 최대값인지 확인
        if int(tmp) > max_val:
            max_val = int(tmp)
    
    answer = str(max_val)
    
    return answer