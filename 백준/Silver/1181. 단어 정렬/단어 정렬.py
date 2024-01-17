import sys
input = sys.stdin.readline
n=int(input())
x=[]

for i in range(n):
    x.append(input())

x=list(set(x))
x.sort()
x.sort(key=len)

for i in x:
    print(i,end='')
