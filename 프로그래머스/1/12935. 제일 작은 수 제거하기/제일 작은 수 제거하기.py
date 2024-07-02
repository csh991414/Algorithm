def solution(arr):
    answer = []
    min = 99999
    for i in arr:
        if i< min:
            min = i
            

    del arr[arr.index(min)]
    
    if len(arr) ==0:
        return [-1]
    else:
        return arr