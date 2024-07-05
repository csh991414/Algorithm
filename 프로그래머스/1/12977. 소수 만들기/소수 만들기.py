import itertools

def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    #print(n)
    return True

def solution(nums):
    answer = 0
    nPr = itertools.combinations(nums, 3)
    for i in nPr:
        if is_prime(sum(i)):
            answer += 1
    return answer
