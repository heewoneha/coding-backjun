import heapq

x = int(input())
heap = [] # asc

for _ in range(x):
    nums = map(int, input().split())

    for num in nums:
        if len(heap) < x:
            heapq.heappush(heap, num)
        else:
            if heap[0] < num:
                heapq.heappop(heap)
                heapq.heappush(heap, num)

print(heap[0])
