#빼먹은거 1
#LRU 알고리즘은 최근 탐색한 페이지를 head 쪽에 저장합니다 (가장 최근에 추가한 페이지처럼)

#cache = 3, input_list = [1, 2, 1, 3, 4, 1, 5, 4] 일 경우,
#세번째 요소인 1을 탐색할 때, [(tail) 1, 2, X (head)] -> [(tail) 2, 1, X (head)] 이렇게 현재 페이지를 가장 최근 탐색한 페이지의 위치로 변경해야 합니다. 

#빼먹은거 22
#초반 cities 배열에서 cacheSize 만큼 집어넣을때 cities 배열의 0번째부터 cacheSize의 인덱스에서 같은 도시가 있을경우가 오류입니다.
#cacheSize : 3 [ "seoul", "seoul", "seoul", "tokyo", "seoul", "tokyo" ]

from collections import deque
def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    for i in range(len(cities)):
        if cacheSize >0: #0보다 캐시크기가 클때만
            if cities[i].lower() not in cache: #큐안에 없음
                if len(cache) >= cacheSize: #큐는 꽉참
                    cache.popleft()
                    cache.append(cities[i].lower())
                    answer+=5
                else: #큐가 꽉 안참
                    cache.append(cities[i].lower())
                    answer+=5
        
            else: #큐안에 있음
                    index_of = cache.index(cities[i].lower())
                    cache.remove(cities[i].lower())
                    cache.append(cities[i].lower())
                    answer+=1
        else: #캐시크기가 0이면
            answer = 5* len(cities)
       
    return answer