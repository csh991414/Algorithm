from collections import deque
def solution(ingredient):
    answer = 0
    burger =[1,2,3,1]
    q=[]
    for i in ingredient:
        q.append(i)
        if q[-4:] == burger:
            answer += 1
            del q[-4:]  # Remove the last 4 elements representing the burger

    return answer
    
    

    return answer