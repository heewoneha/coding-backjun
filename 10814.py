N = int(input()) # 10814번 <나이순 정렬>

what = []

for i in range(0, N):
    age, name = map(str, input().split(" "))
    what.append([int(age), i, str(name)])

what.sort(key = lambda x:x[1]) # 나이 먼저 정렬하면 나중에 뒤섞이니까 순서부터
what.sort(key = lambda x:x[0])

for i in range(0, N):
    print(str(what[i][0]) + " " + what[i][2])