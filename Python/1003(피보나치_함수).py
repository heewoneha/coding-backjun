N = int(input())

for _ in range(0, N):
    dp_zero = [1, 0, 1]
    dp_one = [0, 1, 1]
    
    x = int(input())
    if x == 0 or x == 1 or x == 2:
        print(dp_zero[x], end =' ')
        print(dp_one[x])
    else:
        for i in range(2, x):
            dp_zero.append(dp_zero[i-1] + dp_zero[i])
            dp_one.append(dp_one[i-1] + dp_one[i])
        print(dp_zero[x], end = ' ')
        print(dp_one[x])