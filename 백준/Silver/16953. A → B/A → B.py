import sys
input = sys.stdin.readline
from collections import deque
 
A, B = map(int, input().split())
 
q = deque()
q.append((A, 1))


while q:
    x,count = q.popleft()
    if x== B:
        print(count)
        exit()
    if x*2 <= B:
        q.append((x*2,count+1))
    x =  int(str(x) + "1")
    if x<= B:
        q.append((x,count+1))



print(-1)
