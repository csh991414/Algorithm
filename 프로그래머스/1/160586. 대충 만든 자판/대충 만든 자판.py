def solution(keymap, targets):
    answer = []

    for i in range(len(targets)):
        cnt = 0  
        for j in range(len(targets[i])):
            min_ls = 101  
            for k in keymap:
                pos = k.find(targets[i][j])
                if pos >= 0 and min_ls > pos:
                    min_ls = pos + 1
            
            if min_ls == 101: 
                cnt = 101
                break
            cnt += min_ls
        
        if cnt == 101: 
            answer.append(-1)
        else:  
            answer.append(cnt)
    
    return answer