N = int(input())
balloons = list(map(int, input().split()))
indexs = [i for i in range(1, N+1)]

x = 0
val = balloons.pop(x)
answer = [indexs.pop(x)]

while balloons:
    if val < 0:
        x = (x+val) % len(balloons)
    else:
        x = (x+val-1) % len(balloons)
    val = balloons.pop(x)
    answer.append(indexs.pop(x))

for i in range(0, N):
    print(answer[i], end=' ')
