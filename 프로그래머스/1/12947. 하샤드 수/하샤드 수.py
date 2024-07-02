def solution(x):
    a = list(map(int,list(str(x))))
    b = sum(a)
    if x % b == 0:
        return True
    else:
        return False
    