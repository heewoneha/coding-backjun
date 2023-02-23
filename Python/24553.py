#24553번 <팰린드롬 게임>
T = int(input()) #테스트케이스 개수
for _ in range(0, T): #상윤 -> 승우
    N = int(input()) #돌 무더기 개수
    
    if N % 10 == 0:
        print('1')
    else:
        print('0')