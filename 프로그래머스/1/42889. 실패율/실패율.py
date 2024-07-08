def solution(N, stages):
    answer = []
    
    # 각 스테이지에 머물러 있는 사용자 수를 저장하는 배열
    c = [0] * (N + 1)
    # 각 스테이지를 시도한 사용자 수를 저장하는 배열
    s = [0] * (N + 1)
    # 각 스테이지의 실패율을 저장하는 배열
    rate = [0] * (N + 1)
    
    # 각 스테이지에 머물러 있는 사용자 수를 계산
    for i in stages:
        if i <= N:
            c[i] += 1
    
    # 각 스테이지를 시도한 사용자 수를 계산
    total_players = len(stages)
    for j in range(1, N + 1):
        s[j] = total_players
        total_players -= c[j]
        
    # 각 스테이지의 실패율을 계산
    for l in range(1, N + 1):
        if s[l] != 0:
            rate[l] = c[l] / s[l]
        else:
            rate[l] = 0

    # 실패율을 기준으로 내림차순 정렬, 실패율이 같으면 스테이지 번호 기준으로 오름차순 정렬
    rates = [(rate[i], i) for i in range(1, N + 1)]
    rates.sort(key=lambda x: (-x[0], x[1]))

    # 정렬된 스테이지 번호를 추출
    answer = [x[1] for x in rates]
    return answer
