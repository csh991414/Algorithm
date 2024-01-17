import sys

n=int(sys.stdin.readline())
x=[0]*10001

for i in range(n):
    x[int(sys.stdin.readline())] +=1
for i in range(len(x)):
    if x[i] !=0:
        for j in range(x[i]):
            print(i)
