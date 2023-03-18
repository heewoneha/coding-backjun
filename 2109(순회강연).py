import heapq

n = int(input())
l = []
for _ in range(0, n):
    p, d = map(int, input().split()) # cost, day

    l.append([p, d])

l.sort(key = lambda x: (x[1], -x[0])) # day, cost

lst = []
for x in l:
    heapq.heappush(lst, x[0])
    if len(lst) > x[1]:
        heapq.heappop(lst)

print(sum(lst))