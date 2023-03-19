N, M = map(int, input().split())
l = []

for _ in range(0, N):
    l.append(list(input()))

answer = ''
count = 0
for i in range(0, M):
    dic = {'C': 0 , 'T': 0, 'A': 0, 'G': 0}
    for j in range(0, N):
        dic[l[j][i]] += 1
    
    dic = sorted(dic.items(), key=lambda x: (-x[1], x[0]))

    answer += dic[0][0]
    count += (N-dic[0][1])

print(answer)
print(count)