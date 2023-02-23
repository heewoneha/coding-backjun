def solution(numbers): #16496번 <큰 수 만들기>
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*10, reverse=True)
    return str(int(''.join(numbers)))
N = int(input())
s = list(map(int, input().split()))

print(solution(s))