def solution(newid):
    # 1. 소문자로 변환
    newid = newid.lower()
    
    # 2. 허용된 문자만 필터링
    allowed_chars = "abcdefghijklmnopqrstuvwxyz0123456789-_."
    answer = ''.join(c for c in newid if c in allowed_chars)
    
    # 3. 연속된 마침표를 하나로 줄이기
    answer2 = []
    prev_char = ''
    for char in answer:
        if char == '.' and prev_char == '.':
            continue
        answer2.append(char)
        prev_char = char
    
    # 리스트를 문자열로 변환
    answer2 = ''.join(answer2)
    
    # 4. 문자열의 시작과 끝의 마침표 제거
    if answer2 and answer2[0] == '.':
        answer2 = answer2[1:]
    if answer2 and answer2[-1] == '.':
        answer2 = answer2[:-1]
    
    # 5. 빈 문자열 처리
    if not answer2:
        answer2 = "a"
    
    # 6. 문자열 길이 제한
    if len(answer2) > 15:
        answer2 = answer2[:15]
        if answer2[-1] == '.':
            answer2 = answer2[0:-1]
    
    # 7. 문자열 길이를 최소 3자로 맞추기
    while len(answer2) < 3:
        answer2 += answer2[-1]
    
    return answer2
