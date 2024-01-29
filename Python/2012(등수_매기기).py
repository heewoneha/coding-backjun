N = int(input())
lst = []

for i in range(0, N):
    lst.append(int(input()))

lst.sort()
lst_pair = []
for i in range(0, N):
    lst_pair.append((i+1, lst[i]))

sum_all = 0
for x, y in lst_pair:
    sum_all += abs(x-y)

print(sum_all)
