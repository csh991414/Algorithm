"""
def DFS(numbers,target,depth,values):
    global cnt
    
    if depth == len(numbers) and values == target:
        cnt+=1
        return
    
    elif depth == len(numbers):
        return
    
    DFS(numbers,target,depth+1,values - numbers[depth])
    DFS(numbers,target,depth+1,values + numbers[depth])
    
    

def solution(numbers, target):
    global cnt
    cnt=0
    answer =0
    DFS(numbers,target,0,0)
    
    
    return cnt
"""
#BFS로 풀기
def solution(numbers, target):
    answer=0
    leaves = [0] #모든 계산결과
    
    for num in numbers:
        temp = []
        
        for i in leaves:
            temp.append(i+num)
            temp.append(i-num)
            
        leaves=temp
        
    for i in leaves:
        if i == target:
            answer+=1
    
    return answer
    
    



