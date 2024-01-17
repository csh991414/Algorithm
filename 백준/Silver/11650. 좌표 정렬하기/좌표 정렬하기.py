import sys
input = sys.stdin.readline
n=int(input())
x=[]

for i in range(n):
    [a,b] = map(int,input().split())
    x.append([a,b])
sx=sorted(x)
for i in range(len(x)):
    print(sx[i][0],sx[i][1])