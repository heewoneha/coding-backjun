# 현재 채널은 100
import sys
input = sys.stdin.readline
N = int(input()) # 최종 목적 채널
M = int(input()) # 고장난 버튼 개수
buttons = list(map(int, input().split())) # 고장난 숫자들

minimum = abs(N - 100)

for i in range(0, 1000001):
    x = str(i)
    for j in range(0, len(x)):
        if int(x[j]) in buttons:
            break
        elif j == (len(x) - 1):
            minimum = min(abs(N-i)+len(x), minimum)

print(minimum)