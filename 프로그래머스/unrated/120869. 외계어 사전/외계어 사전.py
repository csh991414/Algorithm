def solution(spell, dic):
    answer = 2
    for i in range(len(dic)):
        cnt=0
        for j in range(len(spell)):
            if spell[j] in dic[i]:
                cnt+=1
                if cnt == len(spell):
                    return 1
    
    return answer