def dfs(cnt, idx, mo_cnt, ja_cnt):
    if cnt == L:
        if mo_cnt >= 1 and ja_cnt >= 2:
            print(''.join(answer))
            return
        else:
            return

    for x in range(idx, C):
        if l[x] in mo:
            answer.append(l[x])
            dfs(cnt + 1, x + 1, mo_cnt + 1, ja_cnt) # idx가 아니라 x
            answer.pop()
        else:
            answer.append(l[x])
            dfs(cnt + 1, x + 1, mo_cnt, ja_cnt + 1) # idx가 아니라 x
            answer.pop()
        

L, C = map(int, input().split()) # C만큼의 길이
l = sorted(list(map(str, input().split())))

mo = ['a', 'e', 'i', 'o', 'u']
answer = []

dfs(0, 0, 0, 0)