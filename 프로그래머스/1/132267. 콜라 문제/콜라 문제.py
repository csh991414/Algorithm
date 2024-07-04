def solution(a, b, n):
    answer = 0
    ahrt =0
    skajwl =0
    
    ahrt = n//a
    skajwl = n%a
    while ahrt*b + skajwl >= a:
        ahrt = n//a
        skajwl = n%a
        answer += ahrt*b
        n = ahrt*b + skajwl
        
        
        print(n,answer)
    
    if a==n:
        answer = b
    
    return answer