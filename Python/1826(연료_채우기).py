import heapq

N = int(input())
q = []

for _ in range(0, N):
    heapq.heappush(q, list(map(int, input().split())))

L, P = map(int, input().split()) # P가 현재 자동차의 연료

count = 0
tmp = []
while P < L:
    while q and q[0][0] <= P:
        loc, l = heapq.heappop(q)
        heapq.heappush(tmp, [-1 * l, loc]) # heap. 휘발유 제일 많이 넣으면서, 가까운

    if not tmp:
        print(-1)
        exit()

    l, loc = heapq.heappop(tmp)
    P += -1 * l
    count += 1

print(count)