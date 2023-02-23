import sys
sys.setrecursionlimit(100000)

def union(a, b):
    x = find(a)
    y = find(b)

    if x != y:
        friend[y] = x
        count[x] += count[y]

def find(x):
    if x == friend[x]:
        return x
    
    parent = find(friend[x])
    friend[x] = parent
    return friend[x]


T = int(input())

for _ in range(0, T):
    F = int(input())
    
    count = {}
    friend = {}

    for i in range(0, F):
        x, y = input().split(' ')

        if x not in friend.keys():
            friend[x] = x # 자기자신
            count[x] = 1
        if y not in friend.keys():
            friend[y] = y
            count[y] = 1
        
        union(x, y)
        print(count[find(x)])