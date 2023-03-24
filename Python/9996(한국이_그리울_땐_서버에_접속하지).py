N = int(input())
x = input().split('*')

pre = x[0]
end = x[1]

for i in range(0, N):
    l = input()
    if l[:len(pre)] == pre:
        if l[-len(end):] == end:
            if len(''.join(x)) <= len(l):
                print('DA')
            else:
                print('NE')
        else:
            print('NE')
    else:
        print('NE')