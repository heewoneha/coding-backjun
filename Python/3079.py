def solution(n, times): #3079번 <입국심사>
    answer = 0
    times.sort()
    
    left = 1
    right = times[len(times) - 1] * n
    
    while (left < right):
        mid = (left + right) // 2; sum_all = 0 #available people
        for t in times:
            sum_all += (mid // t)
            
        if sum_all >= n:
            right = mid
        else:
            left = mid + 1
            
    answer = left
    return answer

N, M = input().split()
N = int(N); M = int(M)
s = []
while(N>0):
    s.append(int(input()))
    N-=1

print(solution(M, s))