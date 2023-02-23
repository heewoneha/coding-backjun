N = int(input()) # 1032번 <명령 프롬프트>

x = list(input())

for i in range(0, N-1):
    y = list(input())

    for j in range(0, len(x)):
        if x[j] != y[j]:
            x[j] = '?'

print(''.join(x))