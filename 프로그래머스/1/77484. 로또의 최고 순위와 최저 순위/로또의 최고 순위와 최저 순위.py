def solution(lottos, win_nums):
    answer = []
    cnt=0
    cnt_0 =0
    for i in lottos:
        
        if i in win_nums:
            cnt+=1
        if i == 0:
            cnt_0 +=1
    if cnt_0 != 6:
        if cnt_0 + cnt ==0:
            return [6,6]
        else:
            answer.append(7-(cnt_0+cnt))

            if cnt_0 == 1 and cnt ==0 :
                answer.append(6)
            else:
                answer.append(7-cnt)
        
    else:
        return [1,6]
    
    
    return answer