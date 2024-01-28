N, M = map(int, input().split())
woods = list(map(int, input().split()))

bottom = 0
top = max(woods)

while bottom <= top:
    mid = (bottom + top) // 2
    
    sum_all = 0
    for i in range(0, N):
        tmp = woods[i] - mid
        if tmp > 0:
            sum_all += tmp
    
    if sum_all >= M:
        bottom = mid + 1
    else:
        top = mid -1
    
print(top)
