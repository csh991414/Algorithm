import sys

n=int(sys.stdin.readline())
x=[]
for i in range(n):
    x.append(int(sys.stdin.readline()))
x= sorted(x)
for i in x:
    print(i)
