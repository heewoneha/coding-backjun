l = list(input())

dic = {}
for i in range(0, len(l)):
    if l[i] not in dic.keys():
        dic[l[i]] = 1
    else:
        dic[l[i]] += 1

mid = ''
count = 0
for x, y in list(dic.items()):
    if y % 2 == 1:
        count += 1
        mid = x
        
        if count >= 2:
            print("I'm Sorry Hansoo")
            exit()

answer = ''    
for x, y in sorted(list(dic.items())):
    answer += (x * (y // 2))
    
print(answer + mid + answer[::-1])