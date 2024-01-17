
n_list = []

for i in range(5):
    num= int(input())
    n_list.append(num)
n_list.sort()
avg = sum(n_list) // 5
print(avg)
print(n_list[2])

