T = int(input())
for _ in range(0, T):
    N = int(input())

    l = []
    for i in range(0, N):
        l.append(list(map(int, input().split())))

    l.sort()

    count = 0
    top = 0

    # 뽑히는 사원이 연속적이지 않을 수 있음
    for i in range(1, N):
        if l[top][1] > l[i][1]: # 순위 비교
            count += 1
            top = i
    
    print(count+1)