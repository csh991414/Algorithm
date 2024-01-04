
def solution(clothes):
    hash_map= {}
    
    for clothe , type in clothes: #앞에거가 옷 이름, 뒤에거가 옷 종류
        # 반대로 자료가 주어지면,  "for type, clothe in clothes" 이렇게 하면됨.
        hash_map[type] = hash_map.get(type,0)+1 #hashmap에 기본은 타입별로 0을 부여하지만, 해당된것이 있으면 1을 추가.
        answer = 1
        for type in hash_map:
            answer *= (hash_map[type]+1) #생각해야할 것 : 2개면 1번 입/2번입/아무것도 안입 총3가지임 그래서 +1
    return answer -1