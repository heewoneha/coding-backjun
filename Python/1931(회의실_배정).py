N = int(input())
l = []

for _ in range(0, N):
    x, y = map(int, input().split())
    l.append((x, y))

l.sort(key=lambda x: (x[1], x[0]))

count = 1
x, y = l[0][0], l[0][1]

for i in range(1, len(l)):
    if y > l[i][0]:
        pass
    else:
        x = l[i][0]
        y = l[i][1]
        count += 1
    
print(count)