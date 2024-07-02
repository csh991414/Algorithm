def solution(price, money, count):
    answer = 0
    p= 0
    for i in range(1,count+1):
        p = p + price
        print(p)
        money -= p
        if money <0 and i == count:
            return -1 * money
        
        
        
    
    
    return answer