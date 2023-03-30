N, M = map(int, input().split())

dic = {}
l = []

for i in range(0, N):
    x = input()
    
    dic[x] = 1


for i in range(0, M):
    x = input()
    
    if x not in dic.keys():
        dic[x] = 1
    else:
        l.append(x)
        dic[x] += 1

l.sort()
print(len(l))
for x in l:
    print(x)