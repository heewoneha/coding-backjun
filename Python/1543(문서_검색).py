l = input()
x = input()

answer = 0
i = 0
while True:
    if i + len(x) <= len(l):
        if l[i:i+len(x)] == x:
            answer += 1
            i += len(x)
        else:
            i += 1
    else:
        break

print(answer)