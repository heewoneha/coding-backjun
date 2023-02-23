import math #1747번 <소수&팰린드롬>

def isPrime(x):
    for i in range(2, int(math.sqrt(x)+1)):
        if x % i == 0:
            return False
    return True

def solution(N):
    result = 0
    for i in range(N, 1000001):
        if i == 1: #2 출력
            continue
        if str(i) == str(i)[::-1]:
            if isPrime(i) == True:
                result = i
                break

    if result == 0:
        result = 1003001 #1000000보다 큰 수이자 팰린드롬&소수

    print(result)

N = int(input())
solution(N)