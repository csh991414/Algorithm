def solution(numbers, hand):
    answer = ''
    rct, lct =[3,0],[3,2] # 현재의 왼손과 오른손 위치
    disl, disr = 0, 0 # 왼쪽 오른쪽 거리저장
    
    for i in numbers:
        if i == 1 or i == 4 or i == 7:
            answer += 'L'
            lct = [(i-1) // 3, 0]  # 왼손 위치 갱신
        elif i == 3 or i == 6 or i == 9:
            answer += 'R'
            rct = [(i-1) // 3, 2]  # 오른손 위치 갱신
        else:  # 가운데줄 2, 5, 8, 0
            if i == 0:
                disl = abs(lct[0] - 3) + abs(lct[1] - 1)
                disr = abs(rct[0] - 3) + abs(rct[1] - 1)
            else:   
                disl = abs(lct[0] - (i-1)//3) + abs(lct[1] - 1)
                disr = abs(rct[0] - (i-1)//3) + abs(rct[1] - 1)

            if disl > disr:
                answer += 'R'
                if i == 0:
                    rct = [3, 1]
                else:
                    rct = [(i-1)//3, 1]
            elif disl < disr:
                answer += 'L'
                if i == 0:
                    lct = [3, 1]
                else:
                    lct = [(i-1)//3, 1]
            else:
                if hand == "right":
                    answer += 'R'
                    if i == 0:
                        rct = [3, 1]
                    else:
                        rct = [(i-1)//3, 1]
                else:
                    answer += 'L'
                    if i == 0:
                        lct = [3, 1]
                    else:
                        lct = [(i-1)//3, 1]
    return answer
