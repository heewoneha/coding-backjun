def solution(phone_book): #5052번 <전화번호 목록>
    answer = True
    
    phone_book.sort()
    
    for i in range(0, len(phone_book) - 1):
        if (phone_book[i] == phone_book[i+1][:len(phone_book[i])]):
            answer = False
    
    return answer

T = int(input())

while(T>0):
    s = []
    N = int(input())
    while(N>0):
        s.append(input())
        N -= 1
    if(solution(s)):
        print('YES')
    else:
        print('NO')
    T -= 1