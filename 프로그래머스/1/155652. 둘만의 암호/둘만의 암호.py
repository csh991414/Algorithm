def solution(s, skip, index):
    answer = ''
    ls= list(s)
    
    for i in range(len(ls)):
        shift_count = 0
        while shift_count < index:
            ls[i] = chr(ord(ls[i]) + 1)
            if ls[i] > 'z':  # 알파벳 범위를 벗어나는 경우 처리
                ls[i] = 'a'
            if ls[i] not in skip:
                shift_count += 1
    
    answer = ''.join(ls)
    return answer