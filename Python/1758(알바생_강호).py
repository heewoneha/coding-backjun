# 팁 == (원래 주려고 생각했던 돈 - 받은 등수 + 1)

N = int(input())
l = []

for _ in range(0, N):
    l.append(int(input()))

l.sort(reverse=True)

tip = 0
for i in range(0, N):
    x = 0
    x = (l[i] - i)

    if x > 0 :
        tip += x

print(tip)