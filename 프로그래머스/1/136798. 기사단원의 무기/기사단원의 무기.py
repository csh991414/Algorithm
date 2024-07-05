def dirtn(n):
    divisorsList = []

    for i in range(1, int(n**(1/2)) + 1):
        if (n % i == 0):
            divisorsList.append(i) 
            if ( (i**2) != n) : 
                divisorsList.append(n // i)

    divisorsList.sort()
    
    return len(divisorsList)

def solution(number, limit, power):
    answer = 0
    ndi=[]
    for i in range(number+1):
        ndi.append(dirtn(i))
    ndi = ndi[1:]
    
    for i in ndi:
        if i <= limit :
            answer +=i
        else:
            answer += power
    
    
    
    return answer