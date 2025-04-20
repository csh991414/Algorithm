from collections import Counter

def solution(want, number, discount):
    answer = 0
    cnt = [0] * len(number)
    chk=0
    for i in range(len(discount)-9):
        di = discount[i:i + 10]
        cnt = [0] * len(number)
        #print(di)
        #print("=================")
        for j in range(len(want)):
            counter = Counter(di)
            want_count = counter[want[j]]
            #print(want_count)
            cnt[j] += want_count
            chk=0
        #print(cnt)
        for k in range(len(number)):
            if number[k] > cnt[k]:
                chk+=1
                break
            else:
                if k==len(number)-1 and chk==0:
                    answer+=1
                    #print("upup")
        
        #print("------------")
    return answer
