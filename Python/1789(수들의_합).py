S = int(input())

sum_all = 0
tmp = 0

while True:
    tmp += 1
    sum_all += tmp
    if sum_all > S:
        break

print(tmp-1)
