import heapq # 1715 <카드 정렬하기>

N = int(input())

l = list()

for i in range(0, N):
    heapq.heappush(l, int(input()))

answer = 0

if len(l) == 1:
    print(0)
else:
    while(len(l) != 1):
        x = heapq.heappop(l)
        y = heapq.heappop(l)

        answer += (x+y)

        heapq.heappush(l, x+y)

    print(answer)