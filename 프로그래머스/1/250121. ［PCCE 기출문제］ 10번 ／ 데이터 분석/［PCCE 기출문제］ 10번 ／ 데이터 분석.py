def solution(data, ext, val_ext, sort_by):
    answer = []

    # 필터링 조건에 따라 데이터 추가
    for item in data:
        if ext == 'date' and item[1] < val_ext:
            answer.append(item)
        elif ext == 'code' and item[0] < val_ext:
            answer.append(item)
        elif ext == 'maximum' and item[2] < val_ext:
            answer.append(item)
        elif ext == 'remain' and item[3] < val_ext:
            answer.append(item)

    # 정렬 조건에 따라 데이터 정렬
    if sort_by == 'remain':
        answer.sort(key=lambda x: x[3])
    elif sort_by == 'maximum':
        answer.sort(key=lambda x: x[2])
    elif sort_by == 'code':
        answer.sort(key=lambda x: x[0])
    elif sort_by == 'date':
        answer.sort(key=lambda x: x[1])

    return answer
