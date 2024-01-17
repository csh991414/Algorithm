import sys
input = sys.stdin.readline
n=int(input())
x=[]

for i in range(n):
    a,b = map(str,input().split())
    x.append([int(a),b])
    
x.sort(key=lambda x:x[0])

for i in x:
    print(*i)
