x = list(input()) # 1251번 <단어 나누기>

answer = []

for i in range (1, len(x)-1):
    for j in range(i+1, len(x)):
        a = x[0:i]
        b = x[i:j]
        c = x[j:]

        a.reverse()
        b.reverse()
        c.reverse()

        a = ''.join(a)
        b = ''.join(b)
        c = ''.join(c)

        answer.append(a+b+c)

answer.sort()

print(answer[0])