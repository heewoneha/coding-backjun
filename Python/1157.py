x = list(input()) # 1157번 <단어 공부>

y = {}

if len(x) > 1:
    for i in range(0, len(x)):
        x[i] = x[i].lower()
        if x[i] in y.keys():
            y[x[i]] += 1
        else:
            y[x[i]] = 1

    y = sorted(y.items(), key = lambda y: y[1], reverse = True)

    if y[0][1] == y[1][1]:
        print('?')
    else:
        print(y[0][0].upper())
else:
    print(x[0].upper())