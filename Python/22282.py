def solution(citations): #22282번 <H-Index>
    citations.sort(reverse=True)
    h_index = 0
    for c in citations:
        if c > h_index:
            h_index += 1
    return h_index

N = int(input())
s = []
while(N>0):
    s.append(int(input()))
    N -= 1

print(solution(s))