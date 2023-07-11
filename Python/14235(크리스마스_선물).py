import heapq

n = int(input())
heap = []

for _ in range(n):
    a = list(map(int, input().split()))
    if a[0] == 0: # meet kids
        if len(heap) == 0:
            print(-1)
        else:
            print(-heapq.heappop(heap))
    else: # charge gifts
        for i in range(1, len(a)):
            heapq.heappush(heap, -a[i])
