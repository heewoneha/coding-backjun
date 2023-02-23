import sys
sys.setrecursionlimit(100000)

def union(a, b):
    x = find(a)
    y = find(b)

    if x < y:
        l[y] = x
    else:
        l[x] = y
        

def find(x):
    if l[x] == x:
        return x
    
    parent = find(l[x])
    l[x] = parent
    return l[x]


N = int(input())
M = int(input())

l = [i for i in range(0, N)]

tmp = []
for i in range(0, N):
    tmp = list(map(int, input().split()))

    for j in range(0, N):
        if tmp[j] == 1:
            union(i, j)

plan = list(map(int, input().split()))
start = plan[0] - 1
for i in range(1, M):
    if l[start] != l[plan[i] - 1]:
        print("NO")
        exit()
print("YES")