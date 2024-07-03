def solution(s, n):
    answer = ''
    
    for i in s:
        if 'a' <= i <= 'z':  # 소문자 범위
            k = ord(i) + n
            if k > ord('z'):
                k = ord('a') + (k - ord('z') - 1)
            answer += chr(k)
        elif 'A' <= i <= 'Z':  # 대문자 범위
            k = ord(i) + n
            if k > ord('Z'):
                k = ord('A') + (k - ord('Z') - 1)
            answer += chr(k)
        else:  # 공백이나 다른 문자
            answer += i
    
    return answer
