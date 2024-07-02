import math
def solution(n):
    answer = 0
    x = math.sqrt(n)
    if int(x) == x:
        return (int(x)+1)**2
    else:
        return -1
    