def solution(nums):
    answer = 0
    temp = set(nums)
    max = len(nums) //2
    
    if max >= len(temp):
        answer = len(temp)
    else:
        answer = max
    
    
    return answer